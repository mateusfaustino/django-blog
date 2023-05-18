from django.shortcuts import render

from post.models import Post

def home(request):

    author = {
        'name':'Mateus de Lucena',
        'description':'Eu sou apenas um rapaz latino americano desbravando o mundo e compartilhando minhas experiências. Quer me conhecer mais? Siga-me em minnhas redes sociais!',
        'avatar':'https://latrilha.com.br/wp-content/uploads/2023/04/322455667_130998663175034_3948680844306346811_n.jpg'
    }

    social_media = [
        {
			'icon':'<svg width="512" height="512" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_305_9)"><path d="M320.669 128.204H191.331C183.043 128.2 174.834 129.829 167.176 132.998C159.517 136.168 152.558 140.815 146.695 146.674C140.833 152.534 136.183 159.491 133.01 167.148C129.837 174.806 128.204 183.013 128.204 191.302V320.64C128.2 328.931 129.83 337.142 133.001 344.802C136.172 352.463 140.822 359.424 146.685 365.286C152.548 371.149 159.508 375.799 167.169 378.97C174.83 382.141 183.04 383.771 191.331 383.767H320.669C328.96 383.771 337.171 382.141 344.832 378.97C352.492 375.799 359.453 371.149 365.316 365.286C371.178 359.424 375.828 352.463 378.999 344.802C382.17 337.142 383.801 328.931 383.797 320.64V191.302C383.797 183.013 382.164 174.806 378.991 167.148C375.818 159.491 371.168 152.534 365.305 146.674C359.443 140.815 352.484 136.168 344.825 132.998C337.166 129.829 328.958 128.2 320.669 128.204ZM256 338.764C239.631 338.764 223.63 333.91 210.019 324.816C196.409 315.721 185.801 302.795 179.537 287.672C173.272 272.549 171.633 255.908 174.827 239.854C178.02 223.799 185.903 209.052 197.478 197.477C209.052 185.903 223.799 178.02 239.854 174.827C255.908 171.633 272.549 173.272 287.673 179.536C302.796 185.801 315.721 196.409 324.816 210.019C333.91 223.629 338.764 239.631 338.764 256C338.733 277.941 330.003 298.974 314.489 314.489C298.974 330.003 277.941 338.733 256 338.764ZM339.229 193.658C335.202 193.658 331.265 192.464 327.916 190.226C324.567 187.989 321.957 184.808 320.416 181.087C318.874 177.366 318.471 173.272 319.257 169.322C320.043 165.372 321.982 161.743 324.83 158.895C327.678 156.047 331.306 154.108 335.257 153.322C339.207 152.536 343.301 152.94 347.022 154.481C350.743 156.022 353.924 158.632 356.161 161.981C358.399 165.33 359.593 169.267 359.593 173.295C359.593 178.695 357.447 183.875 353.629 187.694C349.81 191.513 344.63 193.658 339.229 193.658ZM256 205.411C245.995 205.411 236.214 208.378 227.894 213.937C219.575 219.496 213.091 227.396 209.262 236.64C205.433 245.884 204.431 256.056 206.383 265.87C208.335 275.683 213.153 284.697 220.228 291.772C227.303 298.847 236.318 303.665 246.131 305.617C255.944 307.569 266.116 306.567 275.36 302.738C284.604 298.909 292.505 292.425 298.064 284.106C303.622 275.787 306.589 266.006 306.589 256C306.589 242.583 301.259 229.715 291.772 220.228C282.285 210.741 269.417 205.411 256 205.411ZM320.669 128.204H191.331C183.043 128.2 174.834 129.829 167.176 132.998C159.517 136.168 152.558 140.815 146.695 146.674C140.833 152.534 136.183 159.491 133.01 167.148C129.837 174.806 128.204 183.013 128.204 191.302V320.64C128.2 328.931 129.83 337.142 133.001 344.802C136.172 352.463 140.822 359.424 146.685 365.286C152.548 371.149 159.508 375.799 167.169 378.97C174.83 382.141 183.04 383.771 191.331 383.767H320.669C328.96 383.771 337.171 382.141 344.832 378.97C352.492 375.799 359.453 371.149 365.316 365.286C371.178 359.424 375.828 352.463 378.999 344.802C382.17 337.142 383.801 328.931 383.797 320.64V191.302C383.797 183.013 382.164 174.806 378.991 167.148C375.818 159.491 371.168 152.534 365.305 146.674C359.443 140.815 352.484 136.168 344.825 132.998C337.166 129.829 328.958 128.2 320.669 128.204ZM256 338.764C239.631 338.764 223.63 333.91 210.019 324.816C196.409 315.721 185.801 302.795 179.537 287.672C173.272 272.549 171.633 255.908 174.827 239.854C178.02 223.799 185.903 209.052 197.478 197.477C209.052 185.903 223.799 178.02 239.854 174.827C255.908 171.633 272.549 173.272 287.673 179.536C302.796 185.801 315.721 196.409 324.816 210.019C333.91 223.629 338.764 239.631 338.764 256C338.733 277.941 330.003 298.974 314.489 314.489C298.974 330.003 277.941 338.733 256 338.764ZM339.229 193.658C335.202 193.658 331.265 192.464 327.916 190.226C324.567 187.989 321.957 184.808 320.416 181.087C318.874 177.366 318.471 173.272 319.257 169.322C320.043 165.372 321.982 161.743 324.83 158.895C327.678 156.047 331.306 154.108 335.257 153.322C339.207 152.536 343.301 152.94 347.022 154.481C350.743 156.022 353.924 158.632 356.161 161.981C358.399 165.33 359.593 169.267 359.593 173.295C359.593 178.695 357.447 183.875 353.629 187.694C349.81 191.513 344.63 193.658 339.229 193.658ZM256 205.411C245.995 205.411 236.214 208.378 227.894 213.937C219.575 219.496 213.091 227.396 209.262 236.64C205.433 245.884 204.431 256.056 206.383 265.87C208.335 275.683 213.153 284.697 220.228 291.772C227.303 298.847 236.318 303.665 246.131 305.617C255.944 307.569 266.116 306.567 275.36 302.738C284.604 298.909 292.505 292.425 298.064 284.106C303.622 275.787 306.589 266.006 306.589 256C306.589 242.583 301.259 229.715 291.772 220.228C282.285 210.741 269.417 205.411 256 205.411ZM526.5 91.5491C524.234 70.3549 557.075 15.5694 542 0.500004C526.926 -14.5694 460.195 -55.2407 439 -57.5C329.734 -69.1572 205.266 -31.1573 96.0002 -19.5C74.7842 -17.2657 -20.4019 -23.0716 -35.5 -7.99998C-50.5981 7.07167 -119.709 249.512 -121.981 270.724C-133.638 379.989 -71.6573 432.123 -60 541.389C-57.7707 562.615 -36.5828 621.545 -21.5047 636.649C-6.42664 651.754 153.079 661.23 174.301 663.497C283.564 675.211 311.043 553.261 420.306 541.546C441.53 539.31 505.341 573.857 520.441 558.773C535.54 543.69 583.736 562.612 585.995 541.389C597.661 432.085 538.166 200.853 526.5 91.5491ZM416 320.64C415.985 345.921 405.937 370.163 388.063 388.042C370.19 405.922 345.951 415.977 320.669 416H191.331C166.052 415.969 141.818 405.912 123.946 388.034C106.074 370.156 96.0232 345.919 96.0002 320.64V191.302C96.031 166.031 106.086 141.804 123.958 123.937C141.83 106.07 166.06 96.0231 191.331 96H320.669C345.94 96.0231 370.171 106.07 388.043 123.937C405.915 141.804 415.97 166.031 416 191.302V320.64ZM320.669 128.204H191.331C183.043 128.2 174.834 129.829 167.176 132.998C159.517 136.168 152.558 140.815 146.695 146.674C140.833 152.534 136.183 159.491 133.01 167.148C129.837 174.806 128.204 183.013 128.204 191.302V320.64C128.2 328.931 129.83 337.142 133.001 344.802C136.172 352.463 140.822 359.424 146.685 365.286C152.548 371.149 159.508 375.799 167.169 378.97C174.83 382.141 183.04 383.771 191.331 383.767H320.669C328.96 383.771 337.171 382.141 344.832 378.97C352.492 375.799 359.453 371.149 365.316 365.286C371.178 359.424 375.828 352.463 378.999 344.802C382.17 337.142 383.801 328.931 383.797 320.64V191.302C383.797 183.013 382.164 174.806 378.991 167.148C375.818 159.491 371.168 152.534 365.305 146.674C359.443 140.815 352.484 136.168 344.825 132.998C337.166 129.829 328.958 128.2 320.669 128.204ZM256 338.764C239.631 338.764 223.63 333.91 210.019 324.816C196.409 315.721 185.801 302.795 179.537 287.672C173.272 272.549 171.633 255.908 174.827 239.854C178.02 223.799 185.903 209.052 197.478 197.477C209.052 185.903 223.799 178.02 239.854 174.827C255.908 171.633 272.549 173.272 287.673 179.536C302.796 185.801 315.721 196.409 324.816 210.019C333.91 223.629 338.764 239.631 338.764 256C338.733 277.941 330.003 298.974 314.489 314.489C298.974 330.003 277.941 338.733 256 338.764ZM339.229 193.658C335.202 193.658 331.265 192.464 327.916 190.226C324.567 187.989 321.957 184.808 320.416 181.087C318.874 177.366 318.471 173.272 319.257 169.322C320.043 165.372 321.982 161.743 324.83 158.895C327.678 156.047 331.306 154.108 335.257 153.322C339.207 152.536 343.301 152.94 347.022 154.481C350.743 156.022 353.924 158.632 356.161 161.981C358.399 165.33 359.593 169.267 359.593 173.295C359.593 178.695 357.447 183.875 353.629 187.694C349.81 191.513 344.63 193.658 339.229 193.658ZM256 205.411C245.995 205.411 236.214 208.378 227.894 213.937C219.575 219.496 213.091 227.396 209.262 236.64C205.433 245.884 204.431 256.056 206.383 265.87C208.335 275.683 213.153 284.697 220.228 291.772C227.303 298.847 236.318 303.665 246.131 305.617C255.944 307.569 266.116 306.567 275.36 302.738C284.604 298.909 292.505 292.425 298.064 284.106C303.622 275.787 306.589 266.006 306.589 256C306.589 242.583 301.259 229.715 291.772 220.228C282.285 210.741 269.417 205.411 256 205.411Z" fill="#E68CBE"/></g><defs><clipPath id="clip0_305_9"><rect width="512" height="512" fill="white"/></clipPath></defs></svg>',
			'name':'Instagram',
			'link':''
		},
		{
			'icon':'<svg width="512" height="512" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_305_2)"><rect width="512" height="512" rx="4" fill="#E60000"/><path d="M408.539 179.041C402.139 159.347 380.961 147.419 361.47 144.685C291.364 137.237 220.667 137.237 150.561 144.685C131.07 147.419 109.834 159.23 103.492 179.041C93.514 229.882 93.514 282.178 103.492 333.019C109.892 352.685 131.07 364.641 150.561 367.376C220.667 374.823 291.364 374.823 361.47 367.376C380.961 364.641 402.197 352.83 408.539 333.019C418.517 282.178 418.517 229.882 408.539 179.041ZM223.827 313.594C221.161 315.232 217.732 313.314 217.732 310.186V201.843C217.732 198.715 221.16 196.798 223.826 198.435L312.024 252.608C314.566 254.169 314.566 257.863 312.024 259.425C282.353 277.655 253.376 295.437 223.827 313.594Z" fill="white"/></g><defs><clipPath id="clip0_305_2"><rect width="512" height="512" rx="4" fill="white"/></clipPath></defs></svg>',
			'name':'Youtube',
			'link':''
		},
		{
			'icon':'<svg width="512" height="512" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_305_15)"><rect width="512" height="512" rx="4" fill="#0077B5"/><path d="M184.436 139.636C184.436 148.267 181.877 156.703 177.082 163.879C172.287 171.055 165.472 176.648 157.499 179.951C149.525 183.254 140.752 184.118 132.287 182.434C123.822 180.751 116.047 176.595 109.944 170.492C103.842 164.389 99.6858 156.614 98.0021 148.149C96.3183 139.685 97.1825 130.911 100.485 122.937C103.788 114.964 109.381 108.149 116.557 103.354C123.733 98.5592 132.17 96 140.8 96C152.373 96 163.472 100.597 171.656 108.781C179.839 116.964 184.436 128.063 184.436 139.636ZM174.545 212.364V405.149C174.553 406.571 174.28 407.981 173.741 409.297C173.202 410.613 172.408 411.81 171.405 412.818C170.402 413.827 169.21 414.627 167.896 415.173C166.583 415.719 165.175 416 163.753 416H117.76C116.338 416.004 114.929 415.727 113.614 415.184C112.299 414.642 111.105 413.845 110.099 412.839C109.094 411.833 108.297 410.639 107.754 409.324C107.212 408.009 106.934 406.6 106.938 405.178V212.364C106.938 209.494 108.078 206.741 110.108 204.711C112.137 202.682 114.89 201.542 117.76 201.542H163.753C166.618 201.55 169.363 202.693 171.386 204.722C173.409 206.75 174.545 209.499 174.545 212.364ZM414.953 312.727V406.051C414.957 407.359 414.702 408.654 414.203 409.863C413.705 411.072 412.972 412.17 412.047 413.095C411.123 414.019 410.024 414.752 408.815 415.25C407.607 415.749 406.311 416.004 405.004 416H355.549C354.241 416.004 352.946 415.749 351.737 415.25C350.528 414.752 349.43 414.019 348.505 413.095C347.581 412.17 346.848 411.072 346.349 409.863C345.851 408.654 345.596 407.359 345.6 406.051V315.607C345.6 302.109 349.556 256.495 310.313 256.495C279.913 256.495 273.716 287.709 272.495 301.731V406.051C272.495 408.665 271.467 411.173 269.632 413.035C267.798 414.897 265.304 415.962 262.691 416H214.924C213.618 416 212.326 415.742 211.121 415.242C209.915 414.742 208.82 414.008 207.899 413.084C206.977 412.16 206.247 411.063 205.75 409.856C205.254 408.649 205 407.356 205.004 406.051V211.52C205 210.215 205.254 208.922 205.75 207.715C206.247 206.508 206.977 205.411 207.899 204.487C208.82 203.562 209.915 202.829 211.121 202.329C212.326 201.828 213.618 201.571 214.924 201.571H262.691C265.33 201.571 267.86 202.619 269.726 204.485C271.592 206.351 272.64 208.881 272.64 211.52V228.335C283.927 211.404 300.655 198.342 336.349 198.342C415.418 198.342 414.953 272.175 414.953 312.727Z" fill="white"/></g><defs><clipPath id="clip0_305_15"><rect width="512" height="512" fill="white"/></clipPath></defs></svg>',
			'name':'Linkdin',
			'link':''
        },
	]

    # posts = [
    #     # {
    #     #     'title':'',
    #     #     'excerpt': '',
    #     #     'thumb':'',
    #     #     'link':''
    #     # }
    #     {
    #         'title':'Descubra as melhores atividades para aproveitar ao máximo sua viagem ao Rio de Janeiro',
    #         'excerpt': 'O Rio de Janeiro é uma cidade repleta de atrações turísticas e com uma rica cultura brasileira. Com suas belas praias, morros imponentes e edifícios históricos, é um dos destinos mais procurados por turistas nacionais e internacionais. Se você está planejando uma viagem ao Rio, aqui estão algumas sugestões do que fazer:',
    #         'thumb':'https://latrilha.com.br/wp-content/uploads/2023/04/53.jpg',
    #         'link':'https://latrilha.com.br/2023/04/14/descubra-as-melhores-atividades-para-aproveitar-ao-maximo-sua-viagem-ao-rio-de-janeiro/'
    #     },
    #     {
    #         'title':'8 dicas essenciais para fotografar paisagens e animais selvagens durante trilhas e acampamentos',
    #         'excerpt': 'Fotografar paisagens e animais selvagens durante trilhas e acampamentos pode ser uma experiência emocionante e gratificante. Com a paisagem natural como pano de fundo, é fácil capturar imagens impressionantes que serão apreciadas por anos. Aqui estão algumas dicas de fotografia que podem ajudá-lo a tirar fotos incríveis de paisagens e animais selvagens durante trilhas e camping:',
    #         'thumb':'https://latrilha.com.br/wp-content/uploads/2023/04/51.jpg',
    #         'link':'https://latrilha.com.br/2023/04/01/8-dicas-essenciais-para-fotografar-paisagens-e-animais-selvagens-durante-trilhas-e-acampamentos/'
    #     },
    #     {
    #         'title':'Ecoturismo e conservação ambiental: Como viajantes podem contribuir para a preservação da natureza durante trilhas e viagens',
    #         'excerpt': 'Ecoturismo e conservação ambiental: Informações sobre a importância da preservação ambiental durante as trilhas e viagens, e como os viajantes podem contribuir para a conservação da natureza.',
    #         'thumb':'https://latrilha.com.br/wp-content/uploads/2023/03/latrilha-2.jpg',
    #         'link':'https://latrilha.com.br/2023/03/26/ecoturismo-e-conservacao-ambiental-como-viajantes-podem-contribuir-para-a-preservacao-da-natureza-durante-trilhas-e-viagens/'
    #     }
    # ]

    posts = Post.objects.order_by("post_date").filter(published=True)

    hero_texts = [
        'La Trilha',
        'Aproveite a Paisagem',
        'Ela Passa'
    ]

    context= {
        'hero_texts': hero_texts,
        'posts': posts,
        'social_media': social_media,
        'author': author
    }
    return render(request,'client/home.html',context)