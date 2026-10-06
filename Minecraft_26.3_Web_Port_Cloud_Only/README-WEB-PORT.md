# Minecraft 26.3 — Port real para navegador (cloud-only)

Este pacote foi feito para o repositório que já contém:

`Minecraft_26.3_GitHub_Seguro_Mobile.zip`

## Objetivo

Executar o projeto original no navegador, sem streaming de outro computador e sem exigir build local.

Toda a preparação ocorre no **GitHub Actions** e a saída é publicada no **GitHub Pages**.

## O que já funciona neste estágio

- GitHub Actions extrai o projeto original.
- O `setup`/NeoForm é executado na nuvem.
- O código original é analisado automaticamente.
- Código Java é compilado pelo TeaVM e executa dentro do navegador.
- GitHub Pages hospeda a build.
- O projeto já possui um `<canvas>` destinado ao renderer real.

## O que ainda precisa ser portado para o Minecraft completo abrir

Minecraft Java usa APIs nativas que o navegador não possui diretamente. O relatório gerado a cada build identifica quantas classes dependem de:

- LWJGL / GLFW;
- OpenGL;
- OpenAL;
- JNI;
- sistema de arquivos;
- sockets;
- reflexão.

A estratégia é substituir essas bordas por implementações Web, sem recriar gameplay ou menus.

## Instalação SEM usar PC/terminal local

No GitHub, envie o conteúdo deste ZIP para a raiz do repositório.

Depois:

1. `Settings → Pages → Source`: escolha **GitHub Actions**.
2. Abra `Actions`.
3. Execute **Build Minecraft Web Port**.
4. Aguarde a build.
5. O endereço publicado aparecerá na própria Action.

Nenhuma compilação precisa ser feita no seu computador.

## Tecnologia

O bootstrap usa TeaVM 0.16.0 para compilar Java para código executável no navegador.

A fase seguinte é ligar as APIs do Minecraft às equivalentes Web:

- GLFW → DOM / Pointer Events / Pointer Lock;
- OpenGL → WebGL2 inicialmente, com possibilidade de WebGPU;
- OpenAL → WebAudio;
- arquivos → OPFS/IndexedDB;
- rede incompatível com navegador → camada WebSocket/WebTransport apropriada.

## Importante

O projeto não deve publicar JAR oficial, assets proprietários ou código decompilado da Mojang em repositório público. A Action pode obtê-los durante a build e usá-los temporariamente sem versioná-los no repositório.
