using Microsoft.Extensions.Caching.Memory;

public class AiService
{
    private readonly IMemoryCache _cache;

    public AiService(IMemoryCache cache)
    {
        _cache = cache;
    }

    public async Task<string> AskAsync(string question)
    {
        if (_cache.TryGetValue(question, out string cached))
            return cached;

        // Placeholder for Python / Azure OpenAI call
        var result = $"AI response for: {question}";

        _cache.Set(question, result, TimeSpan.FromMinutes(5));
        return result;
    }
}
