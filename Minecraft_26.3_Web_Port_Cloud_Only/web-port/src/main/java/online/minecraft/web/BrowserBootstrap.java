package online.minecraft.web;

import org.teavm.jso.JSBody;

public final class BrowserBootstrap {
    private BrowserBootstrap() {}

    public static void main(String[] args) {
        setRuntimeStatus("Java → navegador: OK");
        appendLog("TeaVM iniciou código Java dentro do navegador.");
        appendLog("Próximo alvo: substituir dependências nativas LWJGL/GLFW/OpenAL por bridges Web.");
    }

    @JSBody(params = "text", script =
        "const e=document.getElementById('java-runtime-status'); if(e)e.textContent=text;")
    private static native void setRuntimeStatus(String text);

    @JSBody(params = "text", script =
        "const e=document.getElementById('log'); if(e){const d=document.createElement('div');d.textContent=text;e.appendChild(d);}")
    private static native void appendLog(String text);
}
