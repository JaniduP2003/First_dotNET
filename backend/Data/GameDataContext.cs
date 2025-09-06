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

    //SEND DATA TO THE DATABASE
    protected override void OnModelCreating(ModelBuilder modelBuilder)  //This method runs when the database is created.
    {
        modelBuilder.Entity<Genre>().HasData(  //Seed data = initial data that is added to the database when it is created.
            new Genre { Id = 1, Name = "Action" },
            new Genre { Id = 2, Name = "Adventure" },
            new Genre { Id = 3, Name = "RPG" },
            new Genre { Id = 4, Name = "Strategy" }
        );

        modelBuilder.Entity<Game>().HasData(
            new Game { Id = 1, Name = "The Legend of Zelda: Breath of the Wild", GenreId = 2, Price = 59.99m, ReleaseDate = new DateOnly(2017, 3, 3) },
            new Game { Id = 2, Name = "God of War", GenreId = 1, Price = 49.99m, ReleaseDate = new DateOnly(2018, 4, 20) },
            new Game { Id = 3, Name = "The Witcher 3: Wild Hunt", GenreId = 3, Price = 39.99m, ReleaseDate = new DateOnly(2015, 5, 19) },
            new Game { Id = 4, Name = "Civilization VI", GenreId = 4, Price = 29.99m, ReleaseDate = new DateOnly(2016, 10, 21) }
        );
    }

    public DbSet<Game> Games { get; set; }
    public DbSet<Genre> Genres { get; set; }  //DbSet basically = a collection/table of stuff in the database.
}
