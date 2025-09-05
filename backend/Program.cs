using backend.Data;
using backend.Endpoints;
using backend.Entities;


var builder = WebApplication.CreateBuilder(args);

//builder.Configuration Accesses your app’s configuration system, typically appsettings.json in .NET projects
var connString = builder.Configuration.GetConnectionString("GameStore");
builder.Services.AddSqlite<GameDataContext>(connString);

var app = builder.Build();

 
app.MapGamesEndpoints();




app.Run();

