import os
r, w = os.pipe()

pid = os.fork()

if pid > 0:
	print("Parent process is writing")
	text = b"Hello My son"
	os.write(w, text)
	print("Written text:", text.decode())

else:
	os.close(w)
	print("\nChild Process is reading\n")
	r = os.fdopen(r)
	print("Child Read:", r.read())
