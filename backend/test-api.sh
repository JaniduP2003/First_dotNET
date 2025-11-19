#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

API_URL="http://localhost:8080"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Testing Game Store API${NC}"
echo -e "${BLUE}========================================${NC}\n"

# 1. Health check
echo -e "${GREEN}1. Testing /hello endpoint...${NC}"
curl -s $API_URL/hello
echo -e "\n"

# 2. Get all genres
echo -e "${GREEN}2. Getting all genres...${NC}"
curl -s $API_URL/genres | jq '.' || curl -s $API_URL/genres
echo -e "\n"

# 3. Get all games
echo -e "${GREEN}3. Getting all games...${NC}"
curl -s $API_URL/games | jq '.' || curl -s $API_URL/games
echo -e "\n"

# 4. Create a new game
echo -e "${GREEN}4. Creating a new game...${NC}"
CREATE_RESPONSE=$(curl -s -X POST $API_URL/games \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Game",
    "genreId": 1,
    "price": 59.99,
    "releaseDate": "2024-11-19"
  }')
echo $CREATE_RESPONSE | jq '.' || echo $CREATE_RESPONSE
GAME_ID=$(echo $CREATE_RESPONSE | jq -r '.id' 2>/dev/null || echo "1")
echo -e "Created game with ID: $GAME_ID\n"

# 5. Get the newly created game
if [ "$GAME_ID" != "null" ] && [ "$GAME_ID" != "1" ]; then
  echo -e "${GREEN}5. Getting game by ID ($GAME_ID)...${NC}"
  curl -s $API_URL/games/$GAME_ID | jq '.' || curl -s $API_URL/games/$GAME_ID
  echo -e "\n"

  # 6. Update the game
  echo -e "${GREEN}6. Updating game $GAME_ID...${NC}"
  curl -s -X PUT $API_URL/games/$GAME_ID \
    -H "Content-Type: application/json" \
    -d '{
      "name": "Updated Test Game",
      "genreId": 1,
      "price": 39.99,
      "releaseDate": "2024-11-19"
    }'
  echo -e "✓ Update complete\n"

  # 7. Verify the update
  echo -e "${GREEN}7. Verifying the update...${NC}"
  curl -s $API_URL/games/$GAME_ID | jq '.' || curl -s $API_URL/games/$GAME_ID
  echo -e "\n"

  # 8. Delete the game
  echo -e "${GREEN}8. Deleting game $GAME_ID...${NC}"
  curl -s -X DELETE $API_URL/games/$GAME_ID
  echo -e "✓ Delete complete\n"

  # 9. Verify deletion
  echo -e "${GREEN}9. Verifying deletion (should return 404)...${NC}"
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" $API_URL/games/$GAME_ID)
  if [ "$HTTP_CODE" == "404" ]; then
    echo -e "${GREEN}✓ Game successfully deleted (404 response)${NC}\n"
  else
    echo -e "${RED}✗ Unexpected response code: $HTTP_CODE${NC}\n"
  fi
else
  echo -e "${RED}Skipping update/delete tests (could not extract game ID)${NC}\n"
fi

# 10. Final check - Get all games
echo -e "${GREEN}10. Final check - All games:${NC}"
curl -s $API_URL/games | jq '.' || curl -s $API_URL/games
echo -e "\n"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Testing Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
