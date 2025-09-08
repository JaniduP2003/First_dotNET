using backend.Data;
using backend.Dto;
using backend.Entities;
using backend.Mapping;
using Backend.dto;
using Microsoft.EntityFrameworkCore;

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


        public static RouteGroupBuilder MapGamesEndpoints(this WebApplication app)
        {

            var group = app.MapGroup("games").WithParameterValidation();

            group.MapGet("/", () => games);

            group.MapGet("/{id}", (int id) =>
            {

                BackendDto? game = games.Find(game => game.id == id);
                return (game == null) ? Results.NotFound() : Results.Ok(game);  //variable = (condition) ? expressionTrue :  expressionFalse;
                                                                                //Short Hand If...Else (Ternary Operator)

            }).WithName("GetGameById");

            
            // POST: add new gameq
            group.MapPost("/", (CreateGameDto newGame , GameDataContext DbContext) =>
            {

                Game game = newGame.ToEntity();    //the class is in MAPPING FOLDER
                game.Genre = DbContext.Genres.Find(newGame.GenreId);

            
                //games.Add(game); OLD
                DbContext.Games.Add(game);
                DbContext.SaveChanges();                                          //SAVING THE CHAGES TO THE DATABASE


                return Results.CreatedAtRoute("GetGameById", new { id = game.Id }, game.ToDto());

            }).WithParameterValidation();


            //putgames
            group.MapPut("/{id}", (int id, UpdateBackendDto updatedGame) =>
            {

                var index = games.FindIndex(game => game.id == id);

                if (index == -1)
                {
                    return Results.NotFound();
                }


                games[index] = new BackendDto(

                    id,
                    updatedGame.Name,
                    updatedGame.Genre,
                    updatedGame.Price,
                    updatedGame.ReleaseDate
                );

                return Results.NoContent();
            });

            group.MapDelete("/{id}", (int id) =>
            {
                games.RemoveAll(game => game.id == id);
                return Results.NoContent();
            });

            return group;

        }
    }
}