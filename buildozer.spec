[app]

# (str) Title of your application
title = Kasper Hack

# (str) Package name
package.name = kasperhack

# (str) Package domain
package.domain = org.kasper

# (str) Source code where main.py is located
source.dir = .

# (str) Main Python file
source.main = main.py

# (list) List of source files to include
source.include_exts = py,png,jpg,jpeg,kv,json,txt,atlas

# (list) List of source directories to include
source.include_dirs = .

# (str) Application version
version = 1.0

# (list) Python dependencies
# IMPORTANT: do NOT add "android" here
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) Presplash
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]

# (str) Log level
log_level = 2

# (bool) Warn when running as root
warn_on_root = 1


[app:android]

# (str) Android API
android.api = 35

# (str) Android minimum API
android.minapi = 24

# (str) Android NDK
android.ndk = 28c

# (str) Android architecture
android.archs = arm64-v8a

# (str) Android permissions
android.permissions = INTERNET


[buildozer:debug]

# Debug build
android.debug = 1
