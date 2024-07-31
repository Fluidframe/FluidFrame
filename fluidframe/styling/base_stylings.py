from abc import ABC, abstractmethod
from typing import List, Dict, Union, Optional, Tuple



class Style(ABC):
    """
    Abstract base class for styling in various CSS frameworks.
    
    This class provides a flexible interface for applying styles across different
    CSS frameworks. Subclasses should implement these methods according to their
    specific framework's syntax and conventions.

    Attributes:
        theme (str): The current theme ('light' or 'dark').
        css_framework (str): The name of the CSS framework being used.
    """

    def __init__(self, theme: Optional[str] = None, css_framework: str = "tailwind") -> None:
        self.theme = "dark" if theme is None else theme
        self.css_framework = css_framework

    @abstractmethod
    def font(self, size: Optional[Union[str, int, float]] = None, 
             weight: Optional[Union[str, int]] = None, 
             family: Optional[str] = None,
             style: Optional[str] = None,
             variant: Optional[str] = None,
             line_height: Optional[Union[str, int, float]] = None,
             color: Optional[Union[str, Tuple[int, int, int], Dict[str, int]]] = None) -> str:
        """
        Set font-related styles including text color.

        Args:
            size: Font size (e.g., '16px', 1.5, 'large').
            weight: Font weight (e.g., 'bold', 700).
            family: Font family (e.g., 'Arial', 'sans-serif').
            style: Font style (e.g., 'italic', 'normal').
            variant: Font variant (e.g., 'small-caps').
            line_height: Line height (e.g., 1.5, '20px').
            color: Text color (e.g., 'red', '#FF0000', (255, 0, 0), {'r': 255, 'g': 0, 'b': 0}).

        Returns:
            A string of CSS classes or inline styles for font properties.
        """
        pass

    @abstractmethod
    def layout(self, margin: Optional[Union[str, int, Tuple[Union[str, int], ...]]] = None,
               padding: Optional[Union[str, int, Tuple[Union[str, int], ...]]] = None,
               width: Optional[Union[str, int, float]] = None, 
               height: Optional[Union[str, int, float]] = None,
               display: Optional[str] = None,
               position: Optional[str] = None,
               background: Optional[Union[str, Tuple[int, int, int], Dict[str, int]]] = None,
               opacity: Optional[Union[float, int]] = None) -> str:
        """
        Set layout-related styles including background color and opacity.

        Args:
            margin: Margin (e.g., '10px', (10, 20), '1em 2em 3em 4em').
            padding: Padding (e.g., '10px', (10, 20), '1em 2em 3em 4em').
            width: Width (e.g., '100px', 100, '50%').
            height: Height (e.g., '100px', 100, '50%').
            display: Display property (e.g., 'flex', 'block', 'inline-block').
            position: Position property (e.g., 'relative', 'absolute').
            background: Background color (e.g., 'red', '#FF0000', (255, 0, 0), {'r': 255, 'g': 0, 'b': 0}).
            opacity: Opacity value (0 to 1 or 0 to 100).

        Returns:
            A string of CSS classes or inline styles for layout properties.
        """
        pass

    @abstractmethod
    def flex(self, direction: Optional[str] = None, 
             justify: Optional[str] = None, 
             align: Optional[str] = None, 
             wrap: Optional[bool] = None,
             grow: Optional[Union[str, int]] = None,
             shrink: Optional[Union[str, int]] = None,
             basis: Optional[Union[str, int]] = None) -> str:
        """
        Set flex-related styles.

        Args:
        - **`direction`**: Sets the flex direction for the contents of the container.
            - `row`: Sets the flex direction to row (horizontal layout, which is the default).
            - `column`: Sets the flex direction to column (vertical layout).
           
        - **`justify`**: Controls the alignment of items along the main axis (horizontal by default).
            - `start`: Aligns items to the start.
            - `center`: Centers items.
            - `end`: Aligns items to the end.
            - `between`: Distributes items evenly, with space between them.
            - `around`: Distributes items evenly, with space around them.
            - `evenly`: Distributes items evenly, with equal space around them.
            
        - **`align`**: Controls the alignment of items along the cross axis (vertical by default).
            - `start`: Aligns items to the start.
            - `center`: Centers items.
            - `end`: Aligns items to the end.
            - `baseline`: Aligns items along their baseline.
            - `stretch`: Stretches items to fill the container.
                        
        - **`wrap`**: Controls whether items should wrap onto multiple lines.
            - `True`: Enables wrapping of items onto multiple lines.
            - `False`: Prevents items from wrapping (default).
        
        - **`grow`**: Flex grow (e.g., 0, 1, '2').
        - **`shrink`**: Flex shrink (e.g., 0, 1, '2').
        - **`basis`**: Flex basis (e.g., 'auto', '50%', 200).

        Returns:
            A string of CSS classes or inline styles for flex properties.
        """
        pass

    @abstractmethod
    def border(self, width: Optional[Union[str, int]] = None, 
               color: Optional[Union[str, Tuple[int, int, int], Dict[str, int]]] = None, 
               style: Optional[str] = None, 
               radius: Optional[Union[str, int]] = None) -> str:
        """
        Set border-related styles.

        Args:
            width: Border width (e.g., '1px', 2).
            color: Border color (e.g., 'black', '#000000', (0, 0, 0), {'r': 0, 'g': 0, 'b': 0}).
            style: Border style (e.g., 'solid', 'dashed').
            radius: Border radius (e.g., '5px', 5, '50%').

        Returns:
            A string of CSS classes or inline styles for border properties.
        """
        pass

    @abstractmethod
    def spacing(self, gap: Optional[Union[str, int]] = None, 
                space_x: Optional[Union[str, int]] = None, 
                space_y: Optional[Union[str, int]] = None) -> str:
        """
        Set spacing-related styles.

        Args:
            gap: Gap between flex/grid items (e.g., '10px', 10).
            space_x: Horizontal space between elements (e.g., '10px', 10).
            space_y: Vertical space between elements (e.g., '10px', 10).

        Returns:
            A string of CSS classes or inline styles for spacing properties.
        """
        pass

    def combine_styles(self, *styles: str) -> str:
        """
        Combine multiple style strings into a single string.

        Args:
            *styles: Variable number of style strings to combine.

        Returns:
            A single string combining all input styles, with duplicates removed.
        """
        return " ".join(dict.fromkeys(filter(None, styles)))

    @abstractmethod
    def apply_theme(self) -> str:
        """
        Apply theme-specific styles.

        Returns:
            A string of CSS classes or inline styles for the current theme.
        """
        pass
    
    