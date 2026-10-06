#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
from collections import Counter

src = Path(sys.argv[1])
out = Path(sys.argv[2])

patterns = {
    "lwjgl": re.compile(r"\borg\.lwjgl\b"),
    "glfw": re.compile(r"\borg\.lwjgl\.glfw\b|\bGLFW\b"),
    "opengl": re.compile(r"\borg\.lwjgl\.opengl\b|\bGL\d+\b"),
    "openal": re.compile(r"\borg\.lwjgl\.openal\b|\bAL\d+\b"),
    "jni_native": re.compile(r"\bnative\s+[\w<>\[\], ?]+\s+\w+\s*\("),
    "reflection": re.compile(r"\bjava\.lang\.reflect\b|\bClass\.forName\s*\("),
    "filesystem": re.compile(r"\bjava\.nio\.file\b|\bjava\.io\.(File|RandomAccessFile)\b"),
    "sockets": re.compile(r"\bjava\.net\.(Socket|ServerSocket|DatagramSocket)\b"),
}

counts = Counter()
files = 0
java_files = list(src.rglob("*.java")) if src.exists() else []

for f in java_files:
    files += 1
    try:
        text = f.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for name, rx in patterns.items():
        if rx.search(text):
            counts[name] += 1

report = {
    "minecraftSourceFiles": files,
    "blockers": dict(counts),
    "status": "port-in-progress",
    "meaning": {
        "lwjgl": "Classes tied to LWJGL need a browser bridge.",
        "glfw": "Window/input calls need DOM/Pointer Lock/Touch replacements.",
        "opengl": "Rendering calls need WebGL2/WebGPU translation.",
        "openal": "Audio needs WebAudio replacement.",
        "jni_native": "JNI/native methods cannot execute directly in the browser.",
        "reflection": "Reflection may need explicit TeaVM metadata or refactoring.",
        "filesystem": "File access needs OPFS/IndexedDB abstraction.",
        "sockets": "Raw TCP/UDP needs browser-compatible networking/gateway."
    }
}
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report, indent=2))
