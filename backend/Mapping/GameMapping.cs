using System;
using backend.Dto;
using backend.Entities;
using Backend.dto;
using Npgsql.Replication;

namespace backend.Mapping;

public static class GameMapping
{

    public static Game ToEntity(this CreateGameDto game)
    {
        return new Game
        {
            Name = game.Name,
            GenreId = game.GenreId,
            Price = game.Price,
            ReleaseDate = game.ReleaseDate
        };
    }

    public static BackendDto ToDto(this Game game)
    {
                return new(
                    game.Id,
                    game.Name,
                    game.Genre!.Name,
                    game.Price,
                    game.ReleaseDate
                );

    }
}
