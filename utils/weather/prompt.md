# Weather

Get real-time weather and forecast without API key.

## Usage

```bash
# Current weather
weather "New York"
weather "Beijing"

# Forecast
weather "London" --forecast

# Different units
weather "Tokyo" --units metric
weather "Los Angeles" --units imperial
```

## Options

- `--forecast`: Show 5-day forecast
- `--units metric|imperial`: Temperature units
- `--json`: Machine-readable output

## Notes

- No API key required
- Uses free weather data sources
- Location can be city name, zip code, or coordinates
