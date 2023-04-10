
<h1 id="title">Introduction to Quantum Computing</h1>
<p id="Other places to read up">
    Good resouces to understand more: <a class="link" href="https://arxiv.org/abs/quant-ph/0207118"><q>From Cbits to Qbits: Teaching computer scientists quantum mechanics</q></a>.  <a class="link" href="https://youtu.be/In_IL7-qLL4"><q>Introduction to Quantum Computing</q></a> and a  <a class="link" href="https://www.amazon.co.uk/dp/1686230095/ref=cm_sw_em_r_mt_dp_Y.qrFbGSZGQXZ"><q>Quantum Computing Pamphlet</q></a> by Dayton Ellwangner.
</p>
<h2>Part I: A linear algebra recap </h2>
<p >

An understanding of linear algebra is essential to understand all quantum mechanics (QM), because it is the language of quantum mechanics. Learning the basics behind quantum computing is a lot simpler than learning anything else about quantum mechanics because it involves using the simplest quantum system. The qubit. A system with only two defined states, similar to a classic bit. You also never need to understand, yet alone solve the Schr&#246;dinger equation because all quantum systems evolve in a controlled manner (via quantum gates).

</p>
<p>
    Vector space is a collection of vectors. Vectors in vector space can be added together, multiplied (<q>scaled</q>) by numbers, called scalars. Quantum systems are modelled in a vector space with an additional operator called the <b>inner product</b>. The inner product is the general form of the scalar or dot product which you may be familiar with, if not there is an explanation below. Before we go any deeper, I&#8217;m quickly going to go over some linear algebra basics.
</p>
<p>
    Vectors in QM and QC are written in bra-ket or Dirac notation; |v&rang;. Scalers will be written as numbers or letters.
</p>
<p>
    A <b>linear combination</b> is a sum of a group of vectors that have been scaled by a scalar. Eg a|v&rang; + b|u&rang; is a linear combination.
</p>
<p>If any vectors can be written as a linear combination of the others, the vectors a <b>linearly dependant</b>.If vectors cannot be expressed as a linear combination of the others, the vectors are <b>linearly independent</b>. A good analogy which is isomorphic to the two vectors used to represent the states of qubits, is the 2D plane.
</p>
<p>
    Imagine a 2D plane, a vertical vector <b>cannot</b> be expressed in terms of horizontal vectors therefore these vectors are linearly independent. That is, Fig 1 cannot be made of any scalar multiple of Fig 2.
</p>
<div class="row">
    <div class="column">
        <figure>
             ![image](https://user-images.githubusercontent.com/22253343/229457686-993dfa67-bc94-421f-a836-c297d6f8f1bb.png)
             <figcaption>Fig 1</figcaption>
        </figure>
    </div>
    <div class="column">
        <figure>
          ![image](https://user-images.githubusercontent.com/22253343/229457782-aba116c4-2d66-4e0c-b6ce-7819d914f561.png)
          <figcaption>Fig 2</figcaption>
        </figure>
    </div>
  </div>
  <p>
    However, now imagine a diagonal vector. This <b>can</b> be expressed as a sum of horizontal and vertical vectors, multiplied by scalars therefore a system of for example.
  </p>
<div id="centreimg">
  <figure>
      ![image](https://user-images.githubusercontent.com/22253343/229458441-2222781d-4f0f-44dc-982e-bf4cb7518869.png)
      <figcaption>Fig 3</figcaption>
  </figure>
</div>
<p>
    Let Fig 3 represent vector |z&rang;. Let Fig 1 and Fig 2 represent |u&rang; and |v&rang; respectively. |z&rang; can be expressed as |u&rang; + 3.5|v&rang; .
    Any vector in 2D vector space can be written as a |u&rang; and |v&rang;. We say that |u&rang; and |v&rang; <b>span</b> the space, if a set of vectors which are linearly independ can be used to represent every vector in the space they <b>span</b> the space.
    A <b>basis</b> of a vector space is a set of linearly independent vectors which span the space. The <b>dimension</b> of a vector space is the number of vectors in the basis of the vector space. In the above example, there are two so it is a 2-dimensional vector space.
</p>
<p>
    A <b>linear transformation</b> is an operation which transforms one vector into another vector. In QC these vectors will always be in the same vector space. They are linear because they obey the <b>rule of linearity</b>. Let &Ocirc; be a linear transformation. The rule of linearity states that &Ocirc;(a|a&rang; + b|b&rang;) = a&Ocirc;|a&rang; + b&Ocirc;|b&rang;
    A linear transformation can be defined by what it does to the basis vectors of the vector space because all other vectors are linear combinations of these basis vectors.

</p>
<p>
    Back to the inner product space, the scalar/dot product is an operation which acts on two vectors to produce a scalar and is written like &lang;a|b&rang; when acting on vectors |a&rang; and |b&rang;
</p>
<ol>
    The inner product satisfies these three axioms:
    <li>Linearity (for scalars a,b and vectors |u&rang;, |v&rang;, and w |w&rang;), &lang;(a|u&rang; + b|v&rang;)| w&rang; = a&lang;u|w&rang; + b&lang;v|w&rang;                        </li>
    <li>Symmetry, &lang;u|v&rang; = &lang;v|u&rang; = <SPAN STYLE="text-decoration:overline">&lang;v|u&rang;</SPAN>
    </li>
    <li>&lang;u|u&rang;&ge; 0 and = 0 only when u = 0
    </li>
</ol>
<p>
    For vector |x&rang; = 

$$\begin{pmatrix}a1 \\
b1 \\
c1 \\
...
\end{pmatrix}$$ 

  and vector |y&rang; =
  
$$\begin{pmatrix}a2 \\
b2 \\
c2 \\
...
\end{pmatrix}$$ 
  
, &lang;x|y&rang; = a1&times;a2 + b1&times;b2 + c1&times;c2 ...
</p>
<p>
    A <b>normalised</b> vector is one whose inner product with itself is one. Two vectors that are <b>orthogonal</b> if their inner product together is 0, this happens when they are at 90&deg;s/perpendicular to each other. If one vector |a&rang;, and another vector |b&rang; is 90&deg;s from it in any dimension, |b&rang; and |a&rang; will always be linearly independant. Vectors that are normalised and are orthogonal are called orthonormal.

</p>  
<h2>Part II: Quantum Computing</h2>
<h3>Qubits</h3>
<p>
    The <b>Inner Product Space</b> is an extension of vector space with the new operation of the inner product. The world of quantum mechanics is defined in an extension of the Inner Product Space called the Hilbert Space (how these differ is beyond the scope of this post).
</p>
    <p>   A qubit is a quantum system with two distinguishable bases. Qubits are labelled as |0&rang; and |1&rang;. They are defined as orthonormal 2D vectors, therefore spanning the space of single qubits. It is helpful to think of them as the <b>orthonormal vectors</b> |0&rang; => 
 
$$\begin{pmatrix}0 \\
1 
\end{pmatrix}$$ 
  
  and |1&rang; =>
  
$$\begin{pmatrix}1 \\
0 
\end{pmatrix}$$ 
  
  They are analogous and isomorphic to the vectors which are the basis of the 2D plane.
</p>
<p>
    The state of a quantum bit |&psi;&rang;, is  a linear combination of |0&rang; and |1&rang; and two complex numbers a and b: That is, |&psi;&rang; = a|0&rang; + b|1&rang;, (|a|<sup>2</sup> + |b|<sup>2</sup> = 1 because |&psi;&rang;  is normalised). This is possible because qubits can be in a <b>superposition</b> of different states at the same time - a property unique to quantum systems. The value of qubit |&psi;&rang; is a linear combination of the basis values. This means for a one qubit systems it can be in two different states similtaneously.
</p>
<p>
    For 2 qubit systems, the system can be in 4 possible states. A combination of  |0&rang;|0&rang;, |0&rang;|1&rang;, |1&rang;|0&rang;, and |1&rang;|1&rang;, which we will write as |00&rang;, |01&rang;, |10&rang;, and |11&rang; respectively. Therefore this system is modelled by a 4D vector space. Vectors are written right to left, that is the rightmost element is the first qubit. A system with n qubits can take 2<sup>n</sup> states and therefore is modelled in 2<sup>n</sup> dimensional vector space.
</p>
<h3>The Born rule</h3>
<p>
    Having so much possible information to give us a massive amount of more computational possibilities. The state of a qubit could potentially be in any of an infinite amount of different conditions, defined by two complex numbers which satisfy the normalisation criteria. Even though they can contain vast amounts of pontential information you can only ever extract one state.
</p>
<p>
    In quantum mechanics every operation is <b>unitary</b> as a result, therefore every quantum gate has an inverse. There is one exception to this, in classical computing it is so inconsequential it usually isn't even thought of as an operation. This operation is <b>measurement</b>. Classically displaying the information of a system doesn't affect the system, however in quantum mechanics it "collapses" the system. The state of the system is no longer probabilistic but is a defined single state. Repeated measurements will also only extract the same state, it is fixed after it is measured.
    The probability of the system collapsing in a particular state is determined by the complex number &alpha;<sub>x</sub>, which is the amplitude of |x&rang; in the expansion of:
</p>
<p>
  |&psi;&rang; = 
      
$$\sum_{x} a_{x}|x&rang;$$
      
</p>
<p>
  The probability, 
      
$$p_{x}$$
      
</p>
<p>
  The probability, 
  
$$p_{x}$$
      
</p>
<p>
  of it collapsing in state,
  
$$x$$
      
</p>
<p>
  is equal to:

$$p_{x} = |a_{x}|$$<sup>2</sup>
  
</p>
<p>
    This relationship is called the <b>Born Rule</b>. After measurement the system is stuck in that state, so repeated measurements cannot show the overall a representation of the state of the system. Quantum computation is built on increasing the probability of the system collapsing in the desireable (answer) state unlike deterministic classical systems that always reach the correct solution. Fortunately, if by chance it lands on a incorrect state, most quantum computation problems are easy to check if the solution is corrent - like NP-problems. If not you can just re-run the whole computation. Additionally you can just <b>re-run</b> the computation a statistically large amount of time to produce a set of solutions with a very <b>high likelihood</b> of being correct.
</p>
<p>
    The <b>uniform superposition</b>, |s&rang;, is a state where the qubit has an equal chance of collapsing in any of the basis states upon measurement. For a 1 qubit system, it looks like:
</p>
<div class="centre">
<p>|s&rang; = 
      
      
$$\frac{1}{\sqrt{2}}\(|0&rang; + |1&rang;)$$
  
</p>
</div>
<p>
    The square of the magnitude of the amplitudes must be equal over all states, and the sum of the squares of all the amplitudes must equal 1 so we can say for an n qubit system:
</p>
<div class="centre">
<p>
  
$$\frac{1}{\sqrt{2^{n}}}\\sum_{x=0}^{2^{n}-1} |x\rangle$$
  
</p>
</div>
<h3>
    Operations
</h3>
<p>
    Unlike classical bits, which have only two reversible operations that can act on a single bit - the Identity and the Not gate (which flips the value of each bit). Every operation besides measurement is reversible on qubits.
    Quantum gates are linear transformations that act on qubits, these are how quantum computation is implemented. Some are analogous to classical gates such as the quantum not gate. However, the most important quantum gate is the <b>Hadamard gate</b>. When applied it puts the |0&rang; qubit into the uniform superposition.
</p>
<p>
    It is defined as:
</p>
<div class="centre">
<p>
      
$$&Hcirc;|0&rang; = \frac{1}{\sqrt{2}}(|0&rang; + |1&rang;)$$
      
</p>
<p>
  
$$&Hcirc;|1&rang; = \frac{1}{\sqrt{2}}(|0&rang; - |1&rang;)$$

</p>
</div>
<p>Going back to Part I, a linear transformation can be defined over the whole space if it is defined over the base vectors. This means we can calculate what this does to any vector in the vector space representing qubits.</p>
<p>A double implementation of Hadamard gate is the same as the Identity, that is, the Hadamard gate is its own inverse. For example, on |0&rang; transforms it to |s&rang;, a second transforms it back to |0&rang;, proof is trivial and left as exercise for reader ;) .</p>
<p>To put a whole set of qubits into the uniform position requires applying Hadamard to each first we will define function &Hcirc;<sub>i</sub>:</p>
<div class="centre">
    <p>&Hcirc;<sub>i</sub> applies &Hcirc;<sub>n</sub> to the i<sup>th</sup> qubit of a system</p>
</div>
<p>
  
$$&Hcirc;<sub>n</sub>...&Hcirc;<sub>2</sub>&Hcirc;<sub>1</sub>|0...00&rang; =  &Hcirc;<sub>n</sub>....&Hcirc;<sub>2</sub>\(\frac{1}{\sqrt{2}}\)(|0...00&rang; + |0...01&rang;)$$

</p>
<p>
    Hadamard gate is applied to the 1<sup>st</sup> qubit putting it in the uniform super position.
</p>
<p>
    Next we apply the Hadamard gate to the 2<sup>nd</sup> qubit. This puts the |0...00&rang; state into a superposition of:
</p>
<p>
 
 $$\frac{1}{\sqrt{2}}\)(|0...00&rang; + |0...01&rang;)$$

</p>
<p>
   And puts the |0...01&rang; system into a superposition of:
</p>
<div class="centre"><p>\(\frac{1}{\sqrt{2}}\)(|0...01&rang; + |0...11&rang;)</p></div>
<p>Remember this transformation only affects the second qubit of the system</p>
<p> Overall we then get the system in this state:</p>
<div class="centre">
<p>&Hcirc;<sub>n</sub>...&Hcirc;<sub>2</sub>&Hcirc;<sub>1</sub>|0...00&rang; =  &Hcirc;<sub>n</sub>....&Hcirc;<sub>3</sub>\(\frac{1}{\sqrt{2}}\)(\(\frac{1}{\sqrt{2}}\)(|0...00&rang; + |0...01&rang;) + \(\frac{1}{\sqrt{2}}\)(|0...10&rang; + |0...11&rang;))
</p>
</div>
<p>Taking a factor of:
  
 $$\frac{1}{\sqrt{2}}$$
  
out we then get:</p>

<p>
  
$$=  &Hcirc;<sub>n</sub>....&Hcirc;<sub>3</sub>\(\frac{1}{\sqrt{2^{2}}}\)((|0...00&rang; + |0...01&rang;) + (|0...10&rang; + |0...11&rang;))$$

</p>
</div>
<p>If you look at the decimal values of each of the qubit systems you can see they equate to the sequence |1&rang; + |2&rang; + |3&rang; + |3&rang;. Continuing the expansion this pattern continues, creating a sequence of all binary qubit strings up to 2<sup>n</sup>-1. This is because every operation splits each qubit sequence into two seperate possibilities. Each time you apply the Hadamard Gate you also take out a factor of \(\frac{1}{\sqrt{2}}\). We can generalise the uniform superposition of an n length qubit system in this way:</p>
<p>

 $$\frac{1}{\sqrt{2^{n}}}\sum_{x=0}^{2^{n}-1}|x\)&rang;$$
  
where |&xscr;&rang; is the decimal representation of the binary &xscr; in the qubit vector.
  
</p>
</div>
<p>
    The final gate we will cover is the <b>Pauli-Z gate</b>, which here we will denote as &Ocirc;. We can also use this to show how it is possible to increase the probability of a qubit collapsing to a certain state. The Pauli-Z gate is defined as:
</p>
<div class="centre">
    <p>
        &Ocirc;|0&rang; = |0&rang; <br>
        &Ocirc;|1&rang; = -|1&rang;
    </p>
</div>
<p>Now as an example, we are now going to force a one bit uniform superposition of to collapse into the |1&rang; state. So to start and form the uniform superposition you apply &Hcirc; to the |0&rang; qubit to transform it to |s&rang;.</p>
<p>
  
$$&Hcirc;|0&rang; = \frac{1}{\sqrt{2}}\)(|0&rang; + |1&rang;) = |s&rang;$$

</p>

<p>
    Now you apply the &Ocirc; to |s&rang; you change the |1&rang; component to -|1&rang;, which transforms the qubit into the state |s'&rang;.
</p>
<p>

$$&Ocirc;|s&rang; = \(\frac{1}{\sqrt{2}}\)(|0&rang; - |1&rang;) = |s'&rang;$$

</p>

<p>
    This is identical to &Hcirc; acting on |1&rang;, as we previously mentioned &Hcirc; is a self inverse so applying it again will transform the system to |1&rang;
</p>
<p>
  
$$&Hcirc;;|s'&rang; = \(\frac{1}{\sqrt{2}}\)(&Hcirc;|0&rang; - |&Hcirc;1&rang;)$$
  
</p>
<p>
 , this is true because it is a linear transformation therefore obeys linearity.
  
</p>
<p>
  
$$=\frac{1}{\sqrt{2}}\)(\(\frac{1}{\sqrt{2}}\)(|0&rang; + |1&rang;) - \(\frac{1}{\sqrt{2}}\)(|0&rang; - |1&rang;)$$
  
$$= \(\frac{1}{\sqrt{2^{2}}}\)(|0&rang; + |1&rang; - |0&rang; +|1&rang;) = \(\frac{1}{2}\)(2|1&rang;)$$
  
$$=|1&rang;$$
  
 
</p>

<p>This means after applying &Hcirc;&Ocirc;|s&rang; you are guarenteed with a 100% probability to find the state in |1&rang;. Now to a useful application of quantum computing, cracking passwords.</p>
<h2>Part III: Grover&#8217;s Algorithm</h2>
<h3>Coming soon/when I have time...</h3>
</div>

                    
