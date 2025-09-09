using System;
using backend.Dto;
using backend.Entities;

namespace backend.Mapping;

public static class GenreMapping //becouse its a extention class you must add STATIC 
{
    public static GenreDto Todo(this Genre genre) //this makes it an extention method
    {
        return new GenreDto(
            genre.Id,
            genre.Name
        );
    }

}
