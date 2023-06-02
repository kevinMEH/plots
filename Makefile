all: build/$(file)
	./build/$(file)

build/$(file): $(file).c library/*.c
	gcc $(file).c library/*.c -O3 -o build/$(file)

clean:
	rm build/*