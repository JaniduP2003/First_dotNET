using System;
using backend.Entities;
using Microsoft.EntityFrameworkCore;

namespace backend.Data;

public class GameDataContext(DbContextOptions<GameDataContext> options) 
: DbContext
{
  public DbSet<Game> Games => Set<Game>();
  public DbSet<Genre> Genres => Set<Genre>();
}
