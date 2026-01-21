using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/ai")]
public class AiController : ControllerBase
{
    private readonly AiService _service;

    public AiController(AiService service)
    {
        _service = service;
    }

    [HttpPost("ask")]
    public async Task<IActionResult> Ask([FromBody] string question)
    {
        var result = await _service.AskAsync(question);
        return Ok(result);
    }
}
