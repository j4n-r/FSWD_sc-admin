
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

##### Start app

``` bash
 ./run.sh start
```

##### Reset database

``` bash
 ./run.sh reset
```


### Flask commands
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
| Error | `red-500` | `#ef4444` | ![#ef4444](https://placehold.co/20x20/ef4444/ef4444.png) |
| Info | `cyan-500` | `#06b6d4` | ![#06b6d4](https://placehold.co/20x20/06b6d4/06b6d4.png) |

## Neutral Colors
| Color Name | Tailwind Class | Hex Code | Preview |
|------------|----------------|----------|---------|
| Background | `gray-50` | `#f9fafb` | ![#f9fafb](https://placehold.co/20x20/f9fafb/f9fafb.png) |
| Surface | `gray-100` | `#f3f4f6` | ![#f3f4f6](https://placehold.co/20x20/f3f4f6/f3f4f6.png) |
| Border | `gray-300` | `#d1d5db` | ![#d1d5db](https://placehold.co/20x20/d1d5db/d1d5db.png) |
| Text Secondary | `gray-500` | `#6b7280` | ![#6b7280](https://placehold.co/20x20/6b7280/6b7280.png) |
| Text Primary | `gray-700` | `#374151` | ![#374151](https://placehold.co/20x20/374151/374151.png) |
| Text Dark | `gray-900` | `#111827` | ![#111827](https://placehold.co/20x20/111827/111827.png) |
