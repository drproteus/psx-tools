# PSX Tools

Some tools and scripts for working with PSX roms.

|Scripts||
|-|-|
|[m3u\_gen](/scripts/m3u\_gen.py)|generate m3u files for all disc sets in folder|

|Tools|||
|-|-|-|
|`detect-title`|`$FILENAME`|get the Title ID from the disc file|
|`lookup-disc`|`$FILENAME`|lookup the game information by its Title ID from [SerialStation](https://serialstation.com/)|

### Example

```bash
python main.py lookup-disc '~/games/psx/.discs/Final Fantasy IX/Final Fantasy IX (Disc 1).bin'
```
```json
{
  "title_id": "SLUS01251",
  "title_id_type": "SLUS",
  "title_id_number": "01251",
  "name": "Final Fantasy IX",
  "content_type": "Game",
  "systems": [
    "PlayStation 1"
  ],
  "games": [
    {
      "id": "b489ea5b-f5d6-43c7-9ccb-bd182bc8ca47",
      "name": "Final Fantasy IX"
    }
  ]
}
```

### Notes
* Title ID regex borrowed from https://github.com/Nazky/PSXRF
