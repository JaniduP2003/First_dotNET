using backend.Api.dto;
using backend.Dto;


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

app.MapGet("/games", () => games);

app.MapGet("/games/{id}", (int id) =>
    games.Find(game => game.id == id))
    .WithName("GetGameById");

app.MapGet("/janidu", () => "Hello from backend!");

// POST: add new game
app.MapPost("games", (CreateGameDto newGame) =>
{
    backendDto game = new (
        games.Count + 1,
        newGame.Name,
        newGame.Genre,
        newGame.Price,
        newGame.ReleaseDate
    );

    games.Add(game);

    return Results.CreatedAtRoute("GetGameById", new { id = game.id }, game);
});

app.Run();
