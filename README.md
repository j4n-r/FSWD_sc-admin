
# Team Chat

### Members 

**Jan Rueggeberg**

Matr.-Nr.
: 77212019358

**Selin Günaydin**

Matr.-Nr.
: 77211985166

TODO: add instructions for websocket server and env variables 

### Run the app

##### Python venv + install requirements
```bash
 python -m venv venv/ 
 pip install -r requirements.txt
 source venv/bin/activate
```

TODO: Test venv installation (not using flakes)

##### Init db 
```
flask init-db
```

##### Run the app from the root dir
```
flask run --debug
```

### Icons
Pick an icon from (https://lucide.dev/icons/) and click on "Copy SVG"

At the moment tailwindcss via cdn is used, maybe change that in the future.
https://tailwindcss.com/docs/installation/play-cdn

### Style Guide
# Color Palette

# Color Palette

## Primary Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Primary | `blue-500` | `#3b82f6` | ![#3b82f6](https://placehold.co/20x20/3b82f6/3b82f6.png) |
| Primary Dark | `blue-700` | `#1d4ed8` | ![#1d4ed8](https://placehold.co/20x20/1d4ed8/1d4ed8.png) |
| Primary Light | `blue-300` | `#93c5fd` | ![#93c5fd](https://placehold.co/20x20/93c5fd/93c5fd.png) |

## Secondary Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Secondary | `violet-500` | `#8b5cf6` | ![#8b5cf6](https://placehold.co/20x20/8b5cf6/8b5cf6.png) |
| Secondary Dark | `violet-600` | `#7c3aed` | ![#7c3aed](https://placehold.co/20x20/7c3aed/7c3aed.png) |
| Secondary Light | `violet-300` | `#c4b5fd` | ![#c4b5fd](https://placehold.co/20x20/c4b5fd/c4b5fd.png) |

## Accent Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Success | `emerald-500` | `#10b981` | ![#10b981](https://placehold.co/20x20/10b981/10b981.png) |
| Warning | `amber-500` | `#f59e0b` | ![#f59e0b](https://placehold.co/20x20/f59e0b/f59e0b.png) |

## Neutral Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Background | `gray-50` | `#f9fafb` | ![#f9fafb](https://placehold.co/20x20/f9fafb/f9fafb.png) |
| Surface | `gray-100` | `#f3f4f6` | ![#f3f4f6](https://placehold.co/20x20/f3f4f6/f3f4f6.png) |
| Border | `gray-300` | `#d1d5db` | ![#d1d5db](https://placehold.co/20x20/d1d5db/d1d5db.png) |
| Text Secondary | `gray-500` | `#6b7280` | ![#6b7280](https://placehold.co/20x20/6b7280/6b7280.png) |
| Text Primary | `gray-700` | `#374151` | ![#374151](https://placehold.co/20x20/374151/374151.png) |
| Text Dark | `gray-900` | `#111827` | ![#111827](https://placehold.co/20x20/111827/111827.png) |

## Status Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Success | `emerald-600` | `#059669` | ![#059669](https://placehold.co/20x20/059669/059669.png) |
| Warning | `amber-600` | `#d97706` | ![#d97706](https://placehold.co/20x20/d97706/d97706.png) |
| Error | `red-600` | `#dc2626` | ![#dc2626](https://placehold.co/20x20/dc2626/dc2626.png) |
| Info | `sky-600` | `#0284c7` | ![#0284c7](https://placehold.co/20x20/0284c7/0284c7.png) |



TEST
# Color Palette - Variant 2

## Primary Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Primary | `indigo-600` | `#4f46e5` | ![#4f46e5](https://placehold.co/20x20/4f46e5/4f46e5.png) |
| Primary Dark | `indigo-800` | `#3730a3` | ![#3730a3](https://placehold.co/20x20/3730a3/3730a3.png) |
| Primary Light | `indigo-400` | `#818cf8` | ![#818cf8](https://placehold.co/20x20/818cf8/818cf8.png) |

## Secondary Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Secondary | `rose-500` | `#f43f5e` | ![#f43f5e](https://placehold.co/20x20/f43f5e/f43f5e.png) |
| Secondary Dark | `rose-700` | `#be123c` | ![#be123c](https://placehold.co/20x20/be123c/be123c.png) |
| Secondary Light | `rose-300` | `#fda4af` | ![#fda4af](https://placehold.co/20x20/fda4af/fda4af.png) |

## Accent Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Success | `teal-500` | `#14b8a6` | ![#14b8a6](https://placehold.co/20x20/14b8a6/14b8a6.png) |
| Warning | `orange-500` | `#f97316` | ![#f97316](https://placehold.co/20x20/f97316/f97316.png) |

## Neutral Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Background | `slate-50` | `#f8fafc` | ![#f8fafc](https://placehold.co/20x20/f8fafc/f8fafc.png) |
| Surface | `slate-100` | `#f1f5f9` | ![#f1f5f9](https://placehold.co/20x20/f1f5f9/f1f5f9.png) |
| Border | `slate-300` | `#cbd5e1` | ![#cbd5e1](https://placehold.co/20x20/cbd5e1/cbd5e1.png) |
| Text Secondary | `slate-500` | `#64748b` | ![#64748b](https://placehold.co/20x20/64748b/64748b.png) |
| Text Primary | `slate-700` | `#334155` | ![#334155](https://placehold.co/20x20/334155/334155.png) |
| Text Dark | `slate-900` | `#0f172a` | ![#0f172a](https://placehold.co/20x20/0f172a/0f172a.png) |

## Status Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Success | `green-600` | `#16a34a` | ![#16a34a](https://placehold.co/
