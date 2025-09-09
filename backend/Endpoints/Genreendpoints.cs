using System;
using backend.Data;
using backend.Mapping;
using Microsoft.EntityFrameworkCore;
using Npgsql.Replication;

namespace backend.Endpoints;

public static class Genreendpoints
{
    public static RouteGroupBuilder MapGenresEndpoints(this WebApplication app)
    {
        var groupe = app.MapGroup("genres");

        groupe.MapGet("/", async (GameDataContext DbContext) =>
        {
            await DbContext.Genres
                .Select(genre => genre.Todo())
                .ToListAsync();
        });

        return groupe;
    }

}
