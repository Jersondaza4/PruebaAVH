CURL para probar endpoint de GET
curl -X GET "http://127.0.0.1:8000/api/pokemones/?tipo=fuego&numero_mayor_que=50"

CURL para probar endpoint de POST
curl -X POST -H "Content-Type: application/json" -d "[{\"nombre\": \"Eevee\", \"tipo\": \"fuego\", \"numero\": 133}]" "http://127.0.0.1:8000/api/pokemones/add/"