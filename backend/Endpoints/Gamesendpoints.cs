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

            //GET ALL
            group.MapGet("/", async (GameDataContext Dbcontext ) =>
           await Dbcontext.Games.Include(game => game.Genre)
                           .Select(game => game.ToGameSummryDto())
                           .ToListAsync());  //dto IS  A DUMBED DOWN VERSION OF THE ENTITY WITH LESS INFOR AND LESS VERIABLES



            //GET BY ID 
            group.MapGet("/{id}", async(int id , GameDataContext DbContext) => //injected the data context
            {

                Game? game = await DbContext.Games.FindAsync(id);
                return (game == null) ? Results.NotFound() : Results.Ok(game.ToGameDetailsDto());  //variable = (condition) ? expressionTrue :  expressionFalse;
                                                                                //Short Hand If...Else (Ternary Operator)

            }).WithName("GetGameById");

            
            // POST: add new gameq
            group.MapPost("/", async (CreateGameDto newGame , GameDataContext DbContext) =>
            {

                Game game = newGame.ToEntity();    //the class is in MAPPING FOLDER
                game.Genre = DbContext.Genres.Find(newGame.GenreId);

            
                //games.Add(game); OLD
                DbContext.Games.Add(game);
                await DbContext.SaveChangesAsync();                                          //SAVING THE CHAGES TO THE DATABASE


                return Results.CreatedAtRoute("GetGameById", new { id = game.Id }, game.ToGameSummryDto());

            }).WithParameterValidation();


            //putgames
            group.MapPut("/{id}", async (int id, UpdateBackendDto updatedGame , GameDataContext  DbContext) =>
            {

                var existingGame = await DbContext.Games.FindAsync(id);

                if (existingGame is null)
                {
                    return Results.NotFound();
                }

                //THIS IS HOW TO DO THE UPDATE 
                DbContext.Entry(existingGame)
                         .CurrentValues
                         .SetValues(updatedGame.ToEntity(id));

                await DbContext.SaveChangesAsync();

                return Results.NoContent();
            });

            group.MapDelete("/{id}", async (int id , GameDataContext DbContext) =>
            {
                var del_id = await DbContext.Games.FindAsync(id);
                if (del_id is null)
                {
                    return Results.NotFound();
                }
                DbContext.Games.Remove(del_id);
                await DbContext.SaveChangesAsync();
                return Results.NoContent();
            });

            return group;

        }
    }
} //