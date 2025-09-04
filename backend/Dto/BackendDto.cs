namespace Backend.dto;

public record class BackendDto(
    int id,
    string Name,
    string Genre,
    decimal Price,
    DateOnly ReleaseDate

);