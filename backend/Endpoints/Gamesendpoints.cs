using Backend.dto;

namespace backend.Endpoints
{
    public static class Gamesendpoints
    {
        static List<BackendDto> games = new()
        {
            new BackendDto(1, "Game One", "Action", 59.99m,
                DateOnly.FromDateTime(new DateTime(2023, 1, 15))),
            new BackendDto(2, "Game Two", "RPG", 49.99m,
                DateOnly.FromDateTime(new DateTime(2022, 10, 5))),
            new BackendDto(3, "Game Three", "Strategy", 39.99m,
                DateOnly.FromDateTime(new DateTime(2023, 3, 22))),
        };

        // Example method to get all games
        public static IEnumerable<BackendDto> GetAllGames() => games;
    }
}