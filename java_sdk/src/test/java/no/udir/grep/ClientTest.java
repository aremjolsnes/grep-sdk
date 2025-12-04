package no.udir.grep;

import no.udir.grep.models.Laereplan;
import no.udir.grep.models.LaereplanLk20;
import org.junit.jupiter.api.Test;
import java.util.concurrent.ExecutionException;

import static org.junit.jupiter.api.Assertions.*;

public class ClientTest {

    @Test
    public void testGetLaereplanLk20() throws ExecutionException, InterruptedException {
        GrepClient client = new GrepClient();

        // MAT01-05 is Mathematics (LK20)
        Object result = client.getLaereplan("MAT01-05").get();

        assertNotNull(result);
        assertTrue(result instanceof LaereplanLk20, "Expected LaereplanLk20");
        LaereplanLk20 plan = (LaereplanLk20) result;
        assertEquals("MAT01-05", plan.kode);
    }

    @Test
    public void testGetLaereplanLk06() throws ExecutionException, InterruptedException {
        GrepClient client = new GrepClient();

        // RLE1-02 is RLE (LK06), but API returns it on LK20 endpoint too
        Object result = client.getLaereplan("RLE1-02").get();

        assertNotNull(result);
        // API returns LaereplanLk20 for this code now
        if (result instanceof LaereplanLk20) {
            LaereplanLk20 plan = (LaereplanLk20) result;
            assertEquals("RLE1-02", plan.kode);
        } else {
            assertTrue(result instanceof Laereplan, "Expected Laereplan or LaereplanLk20");
            Laereplan plan = (Laereplan) result;
            assertEquals("RLE1-02", plan.kode);
        }
    }
}
