import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  #for i in xrange(X.shape[0]):
  #  X[i,:]-=np.max(X[i,:])
  #sc=X.dot(W)
  #for i in xrange(sc.shape[0]):
    
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in xrange(X.shape[0]):
    sc=np.dot(X[i,:],W)
    sc-=np.max(sc)
    pr=np.exp(sc)/np.sum(np.exp(sc))
    loss+=-np.log(pr[y[i]])
    #pr[y[i]]-=1
    for j in xrange(W.shape[1]):
      p=np.exp(sc[j])/np.sum(np.exp(sc))
      dW[:,j]+=(p-(j==y[i]))*X[i,:]  
         
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  loss/=X.shape[0]
  dW/=X.shape[0]
  loss+=0.5*reg*np.sum(W*W);
  #dw+=reg*W
  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  if X is None:
    return loss,dW
  N=X.shape[0]
  C=W.shape[1]
  
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  sc=X.dot(W)
  sc=sc-np.max(sc,axis=1,keepdims=True)
  prx=np.exp(sc)/np.sum(np.exp(sc),axis=1,keepdims=True)  
  #print 
  loss=-np.sum(np.log(prx[np.arange(N),y]))
  prx[np.arange(prx.shape[0]),y]-=1
  dW=X.T.dot(prx)  
  loss/=N
  dW/=N
  loss+=0.5*reg*np.sum(W*W);
  dW+=reg*np.sum(W)  

  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

