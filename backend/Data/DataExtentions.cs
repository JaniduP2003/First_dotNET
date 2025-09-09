using System;
using Microsoft.EntityFrameworkCore;

namespace backend.Data;

public static class DataExtentions
{
    public static async Task MigrateDbAsync(this WebApplication app)
    {
        using var scope = app.Services.CreateScope();
        var dataContext = scope.ServiceProvider.GetRequiredService<GameDataContext>();
        await dataContext.Database.MigrateAsync();

        //SCOPE : A SCOPE IS A LIFETIME MANAGEMENT TOOL IN DEPENDENCY INJECTION THAT ENSURES S
        // ERVICES ARE CREATED AND DISPOSED OF PROPERLY WITHIN A DEFINED BOUNDARY, SUCH AS A WEB 
        // REQUEST, TO MANAGE RESOURCES EFFICIENTLY AND AVOID MEMORY LEAKS.
        //Scoped	One instance per scope (usually per HTTP request).
    
    //rename the MigrateDb to MigrateDbAsync FOR NAMEING CONVECTION IN .NET
    }

}
