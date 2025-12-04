using Xunit;
using Udir.GrepSdk;
using Udir.GrepSdk.Models;

namespace GrepSdk.Tests;

public class ClientTests
{
    [Fact]
    public async Task GetLaereplan_ShouldReturnLk20Plan_WhenCodeIsLk20()
    {
        // Arrange
        var client = new GrepClient();

        // Act
        // MAT01-05 is Mathematics (LK20)
        var result = await client.GetLaereplanAsync("MAT01-05");

        // Assert
        Assert.NotNull(result);
        Assert.IsType<LaereplanLk20>(result);
        var plan = (LaereplanLk20)result;
        Assert.Equal("MAT01-05", plan.Kode);
    }

    [Fact]
    public async Task GetLaereplan_ShouldReturnLk06Plan_WhenCodeIsLk06()
    {
        // Arrange
        var client = new GrepClient();

        // Act
        // RLE1-02 is RLE (LK06)
        var result = await client.GetLaereplanAsync("RLE1-02");

        // Assert
        Assert.NotNull(result);
        Assert.IsType<LaereplanLk20>(result);
        var plan = (LaereplanLk20)result;
        Assert.Equal("RLE1-02", plan.Kode);
    }
}
