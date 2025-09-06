using backend.Entities;
using Microsoft.EntityFrameworkCore;  //write long and complicated SQL commands this is the middleman makeing thing esay

namespace backend.Data;

public class GameDataContext : DbContext
{
    public GameDataContext(DbContextOptions<GameDataContext> options) : base(options)  //This is a constructor (a special method that runs when you create the 
                                                                                       // object).
                                                                                      //This constructor runs when you make a new GameDataContext object.
    {
    }

    public DbSet<Game> Games { get; set; }
    public DbSet<Genre> Genres { get; set; }  //DbSet basically = a collection/table of stuff in the database.
}
