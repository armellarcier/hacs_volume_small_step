# Volume Small Step — Home Assistant Custom Integration

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz)
[![HA Version](https://img.shields.io/badge/Home%20Assistant-2023.1%2B-blue.svg)](https://www.home-assistant.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Adds `volume_up_small` and `volume_down_small` actions to Home Assistant, allowing fine-grained volume control on any `media_player` entity.

The built-in `media_player.volume_up` / `volume_down` actions are hardcoded to **10% increments** (0.1). This integration lets you use steps as small as 1% — useful for physical buttons, automations, or dashboards where precision matters.

---

## Features

- `volume_small_step.volume_up_small` — increases volume by a configurable step
- `volume_small_step.volume_down_small` — decreases volume by a configurable step
- Optional `step` parameter (default: `0.02`, i.e. 2%)
- Works with any `media_player` entity that exposes `volume_level`
- Fully supports `target:` (entity, device, area)
- Visible in Developer Tools → Actions with a slider UI

---

## Installation

### Via HACS (recommended)

1. Go to **HACS → Integrations → ⋮ → Custom repositories**
2. Add this repository URL and select category **Integration**
3. Click **Download**
4. Restart Home Assistant

### Manual

1. Copy the `volume_small_step/` folder into your `config/custom_components/` directory:
   ```
   config/
   └── custom_components/
       └── volume_small_step/
           ├── __init__.py
           ├── manifest.json
           └── services.yaml
   ```
2. Restart Home Assistant

---

## Configuration

Add the following to your `configuration.yaml`:

```yaml
volume_small_step:
```

No further configuration is required. Restart Home Assistant after adding this line.

---

## Usage

### Basic — default step (2%)

```yaml
action: volume_small_step.volume_up_small
target:
  entity_id: media_player.salon
```

### With a custom step

```yaml
action: volume_small_step.volume_down_small
target:
  entity_id: media_player.salon
data:
  step: 0.05   # 5%
```

### In an automation (physical button)

```yaml
automation:
  - alias: "Bouton volume +"
    trigger:
      - platform: state
        entity_id: binary_sensor.button_volume_up
        to: "on"
    action:
      - action: volume_small_step.volume_up_small
        target:
          entity_id: media_player.salon
        data:
          step: 0.03
```

---

## Parameters

| Parameter | Type   | Required | Default | Range       | Description                     |
|-----------|--------|----------|---------|-------------|---------------------------------|
| `step`    | float  | No       | `0.02`  | 0.01 – 0.5  | Volume increment/decrement size |

The resulting volume is always clamped between `0.0` and `1.0`.

---

## Why not just use `media_player.volume_set` with a template?

You can, and many people do:

```yaml
action: media_player.volume_set
data:
  volume_level: >
    {{ [state_attr('media_player.salon', 'volume_level') + 0.02, 1.0] | min }}
target:
  entity_id: media_player.salon
```

But this approach requires hardcoding the entity ID inside the template — you can't use `target:` generically. This integration works cleanly with areas, device groups, and any number of entities at once, just like the native `volume_up`/`volume_down`.

---

## Compatibility

- Home Assistant **2023.1** and later
- Any `media_player` entity that supports `volume_level` and `media_player.volume_set`

---

## License

MIT