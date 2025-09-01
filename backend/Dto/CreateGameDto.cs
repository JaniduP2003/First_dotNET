namespace backend.Dto;

public record class CreateGameDto(
    //  int id, removed the id becose it is give by the system
    
    string Name,
    string Genre,
    decimal Price,
    DateOnly ReleaseDate
);
