"""Generated from book-content article."""

quantizer = faiss.IndexFlatIP(DIM)
index = faiss.IndexIVFFlat(quantizer, DIM, nlist=100, metric=faiss.METRIC_INNER_PRODUCT)
index.train(image_embeds)
index.add(image_embeds)
index.nprobe = 8  # number of clusters explored per query
