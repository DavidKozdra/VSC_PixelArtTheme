# Change Log

All notable changes to the “dk-file-icons” extension will be documented in this file.

## [Unreleased]

# v7 10/25 

added some changes to the worse sprites git html css java sql and csv 
added a python build step so that the image sizes can be correct and uniform


### Added
- Comprehensive new icons and mappings for:
  - **C**: `.c`, `.h`
  - **C++**: `.cpp`, `.cc`, `.cxx`, `.hpp`, `.hh`, `.hxx`
  - **C#**: `.cs`, `.csproj`, `.sln`
  - **BAT**: `.bat`
  - **Shell scripts**: `.sh`, `.bash`, `.zsh`
  - **Fonts**: `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot`
  - **Music**: `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`
  - **CSV**: `.csv`
- Expanded file-extension coverage for many common aliases (e.g. `.jpeg`, `.bmp`, `.ico`, etc.).
- Environment-file icon mappings for all `.env*` and secrets JSON files.

### Fixed
- JSON sprite loading error.

---

## [3.1.0] – 2025-07-07

### Added
- JSX and TSX support (`.jsx`, `.tsx`) with dedicated icons.
- Environment-lock-file mappings added to the lock-file icon group.

### Changed
- Updated lock-file icon to support multiple variants (`.env.local`, `.env.development`, `.env.production`, `.env.test`).

---

## [3.0.0] – 2025-06-30

### Added
- SQL icon (`.sql`).
- Git-related icons and mappings (`.gitignore`, `.gitattributes`, `.gitmodules`).
- A handful of test images for new file types.

### Changed
- Refreshed default file sprite and reorganized icon definitions for consistency.

---

## [1.0.0] – *Initial release*

- Base icon set: HTML, CSS, JavaScript, TypeScript, JSON, Markdown, Python, Vue, Java, image formats, and generic file/folder icons.
