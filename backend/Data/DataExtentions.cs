using System;
using Microsoft.EntityFrameworkCore;

namespace backend.Data;

public static class DataExtentions
{
    public static void MigrateDb(this WebApplication app)
    {
        using var scope = app.Services.CreateScope();
        var dataContext = scope.ServiceProvider.GetRequiredService<GameDataContext>();
    dataContext.Database.Migrate();
    }

}
