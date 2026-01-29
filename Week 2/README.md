# Tokens, Attention, and Transformer Blocks

## Tokens

Tokens are units of sentences that a transformer can process, or they are the basic unit of information that a transformer can process. They can be words, subwords or characters.

---

## Attention

Attention in Machine Learning is a system of processing the values obtined from embedding tokens in such a way that relevant and important information is preserved.  
It serves as a way to preserve context, so important information (in say a long sequence of text) is not lost along the line. Due to Attention, different embeddings (of inputs) are treated in relation to each other and their relevance as a part of a whole, not merely as an individual token.

---

## Transformer blocks

Transformers are a type of neural network architecture that can process sentences in parallel instead of sequentially, as was the norm in the past.  
They were developed by google in the year 2017. Transformers consist of two parts, the Attention layer and feed forward layer. In the Attention layer, the embeddings from different tokens communicate context while in the feedforward layer, individual embeddings are passed through the network, enabling it to reflect on the meaning of those embeddings.

---

## Simple Flow Diagram

![Transformer Flow Diagram]("Flow Diagram.png")

---


