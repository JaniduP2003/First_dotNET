using backend.Api.dto;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

var games = new List<backendDto>
{
    new backendDto(1, "Game One", "Action", 59.99m,
    DateOnly.FromDateTime(new DateTime(2023, 1, 15))),

    new backendDto(2, "Game Two", "RPG", 49.99m,
    DateOnly.FromDateTime(new DateTime(2022, 10, 5))),

    new backendDto(3, "Game Three", "Strategy", 39.99m,
    DateOnly.FromDateTime(new DateTime(2023, 3, 22))),
};

app.MapGet("games", () => games);
app.MapGet("games/{id}", (int id) => games.Find(game => game.id == id));

// Simple endpoint that returns "Hello World!"
app.MapGet("/janidu", () => "Hello from backend!");

app.Run();
