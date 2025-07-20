
# Team Chat

A web-based real-time messaging application designed for academic environments, enabling professors to manage and moderate student group discussions with full administrative oversight.

## Team Members

| Name | Matriculation Number |
|------|---------------------|
| Jan Rueggeberg | 77212019358 |
| Selin Günaydin | 77211985166 |

## Getting Started

### Prerequisites

The chat functionality is only supported for the following architectures:
- `aarch64-darwin` 
- `x86_64-darwin` 
- `x86_64-linux`

### Installation
#### 1. Set up Python virtual environment
```bash
python3 -m venv venv/ 
source venv/bin/activate
pip install -r requirements.txt
```

#### 2. Initialize the database
If there is no database in the `instance/` directory, run:
```bash
./run.sh reset
# or alternatively
flask init-db
```

#### 3. Start the application
```bash
./run.sh start
```

### Default Users

| Email | Password | Role |
|-------|----------|------|
| admin@admin.com | admin | Administrator |
| test@test.com | test | User |

## Development

### Flask Commands

#### Initialize database
```bash
flask init-db
```

#### Run the app (development mode)
```bash
flask run --debug
```

#### Reset database
```bash
./run.sh reset
```

## Design Resources

### Icons
Pick icons from [Lucide Icons](https://lucide.dev/icons/) and click "Copy SVG"

### Styling
Currently using Tailwind CSS via CDN. See the [Tailwind Play CDN documentation](https://tailwindcss.com/docs/installation/play-cdn) for more information.

## Style Guide
### Color Palette

#### Primary Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Primary | `blue-500` | `#3b82f6` | ![#3b82f6](https://placehold.co/20x20/3b82f6/3b82f6.png) |
| Primary Dark | `blue-700` | `#1d4ed8` | ![#1d4ed8](https://placehold.co/20x20/1d4ed8/1d4ed8.png) |
| Primary Light | `blue-300` | `#93c5fd` | ![#93c5fd](https://placehold.co/20x20/93c5fd/93c5fd.png) |

#### Secondary Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Secondary | `violet-500` | `#8b5cf6` | ![#8b5cf6](https://placehold.co/20x20/8b5cf6/8b5cf6.png) |
| Secondary Dark | `violet-600` | `#7c3aed` | ![#7c3aed](https://placehold.co/20x20/7c3aed/7c3aed.png) |
| Secondary Light | `violet-300` | `#c4b5fd` | ![#c4b5fd](https://placehold.co/20x20/c4b5fd/c4b5fd.png) |

#### Accent Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Success | `emerald-500` | `#10b981` | ![#10b981](https://placehold.co/20x20/10b981/10b981.png) |
| Warning | `amber-500` | `#f59e0b` | ![#f59e0b](https://placehold.co/20x20/f59e0b/f59e0b.png) |
| Error | `red-500` | `#ef4444` | ![#ef4444](https://placehold.co/20x20/ef4444/ef4444.png) |
| Info | `cyan-500` | `#06b6d4` | ![#06b6d4](https://placehold.co/20x20/06b6d4/06b6d4.png) |

#### Neutral Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Background | `gray-50` | `#f9fafb` | ![#f9fafb](https://placehold.co/20x20/f9fafb/f9fafb.png) |
| Surface | `gray-100` | `#f3f4f6` | ![#f3f4f6](https://placehold.co/20x20/f3f4f6/f3f4f6.png) |
| Border | `gray-300` | `#d1d5db` | ![#d1d5db](https://placehold.co/20x20/d1d5db/d1d5db.png) |
| Text Secondary | `gray-500` | `#6b7280` | ![#6b7280](https://placehold.co/20x20/6b7280/6b7280.png) |
| Text Primary | `gray-700` | `#374151` | ![#374151](https://placehold.co/20x20/374151/374151.png) |
| Text Dark | `gray-900` | `#111827` | ![#111827](https://placehold.co/20x20/111827/111827.png) |
