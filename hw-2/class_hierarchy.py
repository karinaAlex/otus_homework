# в проекте мы работаем с медиа-файлами (аудио, видео, фото)
# есть некоторый общий набор данных о файле, необходимый для реализации бизнес-логики (имя, размер, дата создания, владелец...)
# для каждого типа медиа-фалов есть свой набор мета-данных
# попробуйте написать классы для работы с медиа-файлами (они будут основой для пользовательского кода остальных команд)
# приведите примеры кода - как можно создать, обновить, удалить или провести какое-нибудь действие (конвертация, извлечение фич) над файлом (можно без реализации деталей)
# *попробуйте дописать классы для работы с файлами, расположенными не на локальном диске (облако, удаленный сервер, s3-like storage)
# попробуйте ответить на вопросы: много ли кода придется дописать / переписать при добавлении новых типов файлов и способов их хранения?
# !суть задания - именно проектирование классовой иерархии, а не реализация самой логики, поэтому достаточно, например, просто объявить метод .save(...) и в комментарии уточнить - что он должен делать, без конкретной релаизации


