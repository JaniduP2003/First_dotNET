using backend.Data;
using backend.Endpoints;
using backend.Entities;
using Microsoft.EntityFrameworkCore;
using Npgsql.EntityFrameworkCore.PostgreSQL;


var builder = WebApplication.CreateBuilder(args);

//builder.Configuration Accesses your app’s configuration system, typically appsettings.json in .NET projects
builder.Services.AddDbContext<GameDataContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("PostgresConnection")));   //coments on git 

var app = builder.Build();


app.MapGamesEndpoints();
app,MapGenresEndpoints();


 await app.MigrateDbAsync();

app.Run();

