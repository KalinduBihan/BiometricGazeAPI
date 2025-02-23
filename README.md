# Postman Test - Stress Prediction API

## Endpoint
**`POST /predict`**

## Request Body (JSON)
```json
{
  "id": 1,
  "data": [
    {
      "HR": 124.74,
      "TEMP": 31.9,
      "datetime": "2025-02-13 11:13:16"
    },
    {
      "HR": 93.46,
      "TEMP": 31.6,
      "datetime": "2025-02-13 11:13:18"
    },
    {
      "HR": 93.6,
      "TEMP": 31.8,
      "datetime": "2025-02-13 11:13:19"
    },
    {
      "HR": 124.74,
      "TEMP": 31.8,
      "datetime": "2025-02-13 11:13:20"
    },
    {
      "HR": 93.6,
      "TEMP": 31.7,
      "datetime": "2025-02-13 11:13:21"
    },
    {
      "HR": 124.74,
      "TEMP": 31.8,
      "datetime": "2025-02-13 11:13:22"
    },
    {
      "HR": 125,
      "TEMP": 31.9,
      "datetime": "2025-02-13 11:13:23"
    },
    {
      "HR": 125,
      "TEMP": 31.9,
      "datetime": "2025-02-13 11:13:24"
    },
    {
      "HR": 93.6,
      "TEMP": 31.8,
      "datetime": "2025-02-13 11:13:25"
    },
    {
      "HR": 124.74,
      "TEMP": 31.9,
      "datetime": "2025-02-13 11:13:27"
    },
    {
      "HR": 124.74,
      "TEMP": 32.1,
      "datetime": "2025-02-13 11:13:28"
    },
    {
      "HR": 124.74,
      "TEMP": 32.1,
      "datetime": "2025-02-13 11:13:29"
    },
    {
      "HR": 124.74,
      "TEMP": 32,
      "datetime": "2025-02-13 11:13:30"
    },
    {
      "HR": 124.74,
      "TEMP": 32.2,
      "datetime": "2025-02-13 11:13:31"
    },
    {
      "HR": 123.97,
      "TEMP": 32.3,
      "datetime": "2025-02-13 11:13:32"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:33"
    },
    {
      "HR": 124.74,
      "TEMP": 32.3,
      "datetime": "2025-02-13 11:13:34"
    },
    {
      "HR": 124.74,
      "TEMP": 32.3,
      "datetime": "2025-02-13 11:13:36"
    },
    {
      "HR": 125,
      "TEMP": 32.4,
      "datetime": "2025-02-13 11:13:37"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:38"
    },
    {
      "HR": 124.48,
      "TEMP": 32.2,
      "datetime": "2025-02-13 11:13:39"
    },
    {
      "HR": 124.48,
      "TEMP": 32.4,
      "datetime": "2025-02-13 11:13:40"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:41"
    },
    {
      "HR": 93.6,
      "TEMP": 32.3,
      "datetime": "2025-02-13 11:13:42"
    },
    {
      "HR": 124.48,
      "TEMP": 32.4,
      "datetime": "2025-02-13 11:13:43"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:45"
    },
    {
      "HR": 124.74,
      "TEMP": 32.4,
      "datetime": "2025-02-13 11:13:46"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:47"
    },
    {
      "HR": 124.74,
      "TEMP": 32.4,
      "datetime": "2025-02-13 11:13:48"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:49"
    },
    {
      "HR": 124.48,
      "TEMP": 32.5,
      "datetime": "2025-02-13 11:13:50"
    },
    {
      "HR": 93.46,
      "TEMP": 32.5,
      "datetime": "2025-02-13 11:13:51"
    },
    {
      "HR": 124.48,
      "TEMP": 32.4,
      "datetime": "2025-02-13 11:13:52"
    },
    {
      "HR": 124.74,
      "TEMP": 32.5,
      "datetime": "2025-02-13 11:13:54"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:55"
    },
    {
      "HR": 125,
      "TEMP": 32.8,
      "datetime": "2025-02-13 11:13:56"
    },
    {
      "HR": 124.74,
      "TEMP": 32.6,
      "datetime": "2025-02-13 11:13:57"
    },
    {
      "HR": 124.74,
      "TEMP": 32.7,
      "datetime": "2025-02-13 11:13:58"
    }
  ]
}
```

## Expected Response (JSON)
```json
{
  "average_stress": "73.40%",
  "id": 1,
  "stress": "Adequate"
}
```

## Notes
- This request sends heart rate (HR) and temperature (TEMP) data to the `/predict` endpoint.
- The response provides the **average stress percentage** and **stress level classification**.
```
