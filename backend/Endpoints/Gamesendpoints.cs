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
      

        public static RouteGroupBuilder MapGamesEndpoints(this WebApplication app)
        {

            var group = app.MapGroup("games").WithParameterValidation();

            group.MapGet("/", (GameDataContext Dbcontext ) =>
            Dbcontext.Games.Include(game => game.Genre).Select(game => game.ToGameSummryDto()));  //dto IS  A DUMBED DOWN VERSION OF THE ENTITY WITH LESS INFOR AND LESS VERIABLES



            //GET BY ID 
            group.MapGet("/{id}", (int id , GameDataContext DbContext) => //injected the data context
            {

                Game? game = DbContext.Games.Find(id);
                return (game == null) ? Results.NotFound() : Results.Ok(game.ToGameDetailsDto());  //variable = (condition) ? expressionTrue :  expressionFalse;
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


                return Results.CreatedAtRoute("GetGameById", new { id = game.Id }, game.ToGameSummryDto());

            }).WithParameterValidation();


            //putgames
            group.MapPut("/{id}", (int id, UpdateBackendDto updatedGame , GameDataContext  DbContext) =>
            {

                var existingGame = DbContext.Games.Find(id);

                if (existingGame is null)
                {
                    return Results.NotFound();
                }

                //THIS IS HOW TO DO THE UPDATE 
                DbContext.Entry(existingGame)
                         .CurrentValues
                         .SetValues(updatedGame.ToEntity(id));
                DbContext.SaveChanges();

                return Results.NoContent();
            });

            group.MapDelete("/{id}", (int id , GameDataContext DbContext) =>
            {
                var del_id = DbContext.Games.Find(id);
                if (del_id is null)
                {
                    return Results.NotFound();
                }
                DbContext.Games.Remove(del_id);
                DbContext.SaveChanges();
                return Results.NoContent();
            });

            return group;

        }
    }
}