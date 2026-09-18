# The Kinetic Engine — Student Workspace

## What You're Building

You'll implement the core movement system for a 3D samurai game. When done, your character will walk through a procedurally generated world, collect items, and level up — all powered by code you write.

## Setup

```bash
npm install
npm run dev
```

Opens at `http://localhost:4004`

## Your Task

Open `src/student.js` — this is the **only file you edit**.

You have 5 functions to implement:

| Task | Function | What it does |
|------|----------|--------------|
| 1 | `createPlayer(startX, startY)` | Build the player object with all required fields |
| 2 | `movePlayer(player, direction, tiles)` | Move one tile in a direction with collision |
| 3 | `getSpeedMultiplier(player, tiles)` | Return terrain speed (forest = slow, path = fast) |
| 4 | `collectItem(player, item)` | Apply coin/potion effect, return message |
| 5 | `checkLevelUp(player)` | Level up when XP threshold is reached |

## How It Works

- The game engine calls your functions directly — no fallbacks
- If a function is wrong or empty, the game will crash or behave incorrectly
- Walk over items to collect them (auto-collect on proximity)
- The speed indicator (top right) shows your `getSpeedMultiplier()` result live

## Controls

| Key | Action |
|-----|--------|
| WASD / Arrow keys | Move |
| Mouse drag | Rotate camera |
| Scroll | Zoom |
| Click | Lock cursor |
| ESC | Release cursor |

## Reference

All helper functions and constants are in `src/engine.js` (read-only):
- `TILE_S` — tile size in pixels (48)
- `WORLD_W`, `WORLD_H` — world dimensions
- `isWalkable(tileType)` — returns true if tile can be walked on
- `speedMult(tileType)` — returns speed multiplier for a tile type
- `T` — tile type constants (T.GRASS, T.FOREST, T.PATH, etc.)

## Tips

- `createPlayer` must return an object with **all** listed fields or the game won't start
- `movePlayer` receives a 2D array: `tiles[ty][tx]`
- `checkLevelUp` threshold = `player.level * 150`
- Use spread syntax to return updated objects: `{ ...player, gold: player.gold + 10 }`
