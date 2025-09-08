using System.ComponentModel.DataAnnotations;

namespace backend.Dto;

public record class CreateGameDto(
    //  int id, removed the id becose it is give by the system
    
    [Required][StringLength(50)]string Name,
    int GenreId,
    [Range(0,100)]decimal Price,
    DateOnly ReleaseDate
);
