
curl -s "https://api.spotify.com/v1/albums/62VlldLNKK8OGw8vbyIFED/tracks?limit=50" -H "Authorization: Bearer $token" | jq -r '.items[]| [.name, .id] | @csv'  
