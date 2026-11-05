#!/usr/bin/env bash
set -e

# ==============================================================================
# Automated Android Build & Export Script for Chinese Vocal HSK 5 Lexicon
# ==============================================================================

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "=== [1/6] Setting up Build Environment ==="

# 1. Java 21 LTS Setup
if [ -d "/usr/local/sdkman/candidates/java/21.0.13.0+2-ms" ]; then
    export JAVA_HOME="/usr/local/sdkman/candidates/java/21.0.13.0+2-ms"
elif [ -z "$JAVA_HOME" ]; then
    if command -v java >/dev/null 2>&1; then
        export JAVA_HOME="$(dirname "$(dirname "$(readlink -f "$(which java)")")")"
    fi
fi
export PATH="$JAVA_HOME/bin:$PATH"
echo "Using Java: $(java -version 2>&1 | head -n 1)"

# 2. Android SDK Setup
if [ -z "$ANDROID_HOME" ]; then
    if [ -d "/home/codespace/android-sdk" ]; then
        export ANDROID_HOME="/home/codespace/android-sdk"
    elif [ -d "$HOME/Android/Sdk" ]; then
        export ANDROID_HOME="$HOME/Android/Sdk"
    else
        echo "Android SDK not found. Setting up in /home/codespace/android-sdk..."
        export ANDROID_HOME="/home/codespace/android-sdk"
        mkdir -p "$ANDROID_HOME/cmdline-tools"
        if [ ! -d "$ANDROID_HOME/cmdline-tools/latest" ]; then
            curl -sS -o /tmp/cmdline-tools.zip https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
            unzip -q /tmp/cmdline-tools.zip -d /tmp/cmdline-tools-unpacked
            mv /tmp/cmdline-tools-unpacked/cmdline-tools "$ANDROID_HOME/cmdline-tools/latest"
            rm -rf /tmp/cmdline-tools.zip /tmp/cmdline-tools-unpacked
        fi
        yes | "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" --licenses > /dev/null 2>&1 || true
        "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" "platform-tools" "platforms;android-35" "build-tools;34.0.0"
    fi
fi
echo "Using Android SDK: $ANDROID_HOME"

echo "=== [2/6] Compiling Lexicographical Data ==="
python3 cli.py build

echo "=== [3/6] Bundling Web Distribution Assets ==="
rm -rf www
mkdir -p www/web www/data www/chapters
cp index.html www/
cp -r web/* www/web/
cp -r data/* www/data/
cp -r chapters/* www/chapters/
# Strip source generation code and raw .toon files from final mobile bundle
rm -rf www/chapters/*/generators www/chapters/*/words www/chapters/*/*.csv

echo "=== [4/6] Syncing with Capacitor Android ==="
npx cap sync android

echo "=== [5/6] Assembling Android Debug APK via Gradle ==="
cd android
./gradlew assembleDebug
cd "$ROOT_DIR"

echo "=== [6/6] Exporting APK to exports/ ==="
mkdir -p exports
cp android/app/build/outputs/apk/debug/app-debug.apk exports/chinese-vocal-hsk-v1.1-debug.apk
cp android/app/build/outputs/apk/debug/app-debug.apk exports/chinese-vocal-hsk-v1.0-debug.apk
cp android/app/build/outputs/apk/debug/app-debug.apk exports/chinese-vocal-hsk-debug.apk
cp android/app/build/outputs/apk/debug/app-debug.apk exports/hsk5-vocal-lexicon-debug.apk

APK_SIZE=$(du -h exports/chinese-vocal-hsk-v1.1-debug.apk | cut -f1)
echo ""
echo "=============================================================================="
echo " [SUCCESS] Android Export Complete!"
echo " APK Output : $ROOT_DIR/exports/chinese-vocal-hsk-v1.1-debug.apk ($APK_SIZE)"
echo " Project    : $ROOT_DIR/android/ (Ready for Android Studio)"
echo "=============================================================================="
echo "To install on a connected Android phone or emulator:"
echo "  adb install -r exports/chinese-vocal-hsk-v1.0-debug.apk"
echo "=============================================================================="
