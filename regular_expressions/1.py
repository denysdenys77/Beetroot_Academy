# Извлечь все слова, которые начинаются на гласную букву из текста https://ru.lipsum.com/feed/html

import re
from re import IGNORECASE


lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In a tortor ut est pulvinar suscipit. Duis ' \
        'tristique varius lorem, in ultrices nunc auctor et. Aliquam nulla ex, dapibus quis laoreet eu, consectetur ' \
        'in lorem. Mauris vulputate diam ac ultrices elementum. Vivamus sit amet fringilla mi. Mauris quis nisi ' \
        'convallis, interdum urna sit amet, egestas libero. Fusce aliquam felis diam, quis condimentum tortor dictum ' \
        'vel. Praesent nec mi convallis enim suscipit laoreet. Mauris eget magna eget lectus imperdiet egestas. In ' \
        'velit nisl, sodales eu ligula sit amet, sagittis lobortis sem. Vestibulum lectus turpis, finibus nec tempor ' \
        'nec, rutrum a ligula. Sed iaculis leo in sapien tincidunt, vitae auctor erat feugiat. Ut elementum justo ' \
        'sed tortor eleifend, eu volutpat dui finibus. Integer tincidunt magna ipsum. Nunc non libero a mi consectetur ' \
        'mattis. Nulla id arcu nec urna cursus ultricies. Phasellus lacinia gravida dictum. Vestibulum varius sed ' \
        'justo et tempor. Morbi ornare nulla nisi, vel consequat augue fermentum vitae. Etiam justo leo, dictum at ' \
        'erat viverra, eleifend placerat nisl. Sed felis magna, consequat in imperdiet nec, egestas et turpis. Cras ' \
        'faucibus, urna finibus feugiat tincidunt, orci nisi iaculis ex, quis accumsan neque purus et leo. Sed ' \
        'feugiat eros sed magna sollicitudin laoreet. In id finibus tortor, blandit maximus justo. Suspendisse ' \
        'volutpat blandit eros id vehicula. Vivamus congue facilisis neque quis pharetra. Suspendisse lacinia, mauris ' \
        'eget aliquet lacinia, ipsum diam ornare eros, at lacinia lacus justo eu arcu. Pellentesque consectetur ' \
        'eros sed elit euismod, eget congue ex bibendum. Class aptent taciti sociosqu ad litora torquent per conubia ' \
        'nostra, per inceptos himenaeos. Mauris sagittis libero vel nunc ultricies eleifend. Mauris ex velit, lacinia ' \
        'quis laoreet vel, feugiat sit amet sem. Curabitur rhoncus enim sed eros rhoncus, et scelerisque mauris ' \
        'venenatis. Pellentesque leo orci, volutpat a suscipit sit amet, interdum sit amet arcu. Donec placerat ' \
        'vel sem vitae fringilla. Nam quis ullamcorper dui. Mauris massa turpis, elementum id turpis id, pharetra ' \
        'condimentum leo. Donec euismod bibendum dui. Nunc elementum ac est quis efficitur. In ante eros, pharetra ' \
        'et elementum at, sollicitudin nec justo. Etiam enim nulla placerat feugiat hendrerit vitae, condimentum ' \
        'nec dolor. Etiam felis lectus, efficitur non gravida a, efficitur ut diam. Aenean eget libero tincidunt, ' \
        'venenatis ligula nec, consectetur magna. Praesent in tempor diam. Nam id velit vel est fermentum feugiat. ' \
        'Ut consequat ipsum ut imperdiet fermentum. Curabitur vehicula venenatis dictum. Integer a lectus elit. ' \
        'Maecenas vitae odio vel neque placerat porta. Fusce vitae ipsum non lacus faucibus scelerisque. Maecenas ' \
        'ut felis a dui pulvinar porttitor. Vivamus euismod dui odio, eu vulputate diam efficitur sed. '


result = re.findall(r'\b[yuoiea]\w+', lorem, flags=IGNORECASE)
print(result)

# yuoiea
# аеiouy