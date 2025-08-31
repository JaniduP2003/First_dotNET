var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

// Simple endpoint that returns "Hello World!"
app.MapGet("/hello", () => "Hello from backend!");

app.Run();
