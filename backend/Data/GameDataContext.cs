using backend.Entities;
using Microsoft.EntityFrameworkCore;

namespace backend.Data;

public class GameDataContext : DbContext
{
    public GameDataContext(DbContextOptions<GameDataContext> options) : base(options)
    {
    }

    public DbSet<Game> Games { get; set; }
    public DbSet<Genre> Genres { get; set; }
}
