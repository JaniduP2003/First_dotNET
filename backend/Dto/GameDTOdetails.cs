using System;

namespace backend.Dto;

public record class GameDTOdetails
(
     int id,
    string Name,
    int GenreId,
    decimal Price,
    DateOnly ReleaseDate
    
);


