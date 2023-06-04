
import py4j.GatewayServer;

public class TextCombiner {

    public static String combineTexts(String[] texts) {
        if (texts == null || texts.length == 0) {
            return "";
        }
        String result = texts[0];
        for (int i = 1; i < texts.length; i++) {
            String overlap = "";
            for (int j = 0; j < result.length(); j++) {
                if (texts[i].startsWith(result.substring(j))) {
                    overlap = result.substring(j);
                    break;
                }
            }
            for (int j = overlap.length(); j > 0; j--) {
                if (texts[i].endsWith(overlap.substring(0, j))) {
                    result = result + texts[i].substring(overlap.length() - j);
                    break;
                }
            }
            if (overlap.isEmpty()) {
                result = result + texts[i];
            } else {
                result = result + texts[i].substring(overlap.length());
            }
        }
        return result;
    }

    public static void main(String[] args) {

        TextCombiner combiner = new TextCombiner();

        GatewayServer server = new GatewayServer(combiner);
        server.start();
        System.out.println("Gateway Server Started");
//        String text1 = "ahmet eve geldin mi";
//        String text2 = "eve geldiniz mi";
//        String result = combineTexts(text1, text2);
//        System.out.println(result);
    }
}
